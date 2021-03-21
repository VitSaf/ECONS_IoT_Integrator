from concurrent import futures
import logging
import grpc
import iiot_device_pb2
import iiot_device_pb2_grpc
from datetime import datetime,timedelta
from google.protobuf.timestamp_pb2 import Timestamp
import mes_data as md
from mes_data import toXML, getConfigData
import configparser
import requests


#Основной скрипт, где описаны главные функции для связи с серверами
#Здесь же происходят вызовы этих функций( в конце)

#сервер iiot
IOT_IP = ''
#сервер аутентификации
URL_PROD_CLOAK = 'https://s001dp-0093.dev002.local/auth/realms/sibur/protocol/openid-connect/token'
#разница между временем сервера iiot и "ЭКОНС"(сколько часов добавить ко времени, полученному с iiot)
HOURS_BETWEEN_SERVERS = 3

#Для аутентификации
login = ''
password = ''


#функция, собирающая объект для передачи по grpc (в соотвествии с proto файлом) с инфо по датчикам,
#данные для которых мы запрашиваем
def proto(euis, token):
	#создаем объект из автогенерированного класса
	msg = iiot_device_pb2.DeviceDataRequest()
	msg.token = token
	#выставляем поля объекта - токен и список устройств, которые сейчас подключены к ИоТ серверу (датчики)
	for i in euis:
		msg.devEuiList.append(i)
	return msg

#создаем grpc канал в соотвествии с документацией протокола
#https://grpc.io/docs/languages/python/basics/
def getChannel():
	return grpc.insecure_channel(IOT_IP)

#получаем список всех датчиков зарегестрированных на сервере ИоТ
def getDevices(channel, token):
#по принципу протокола grpc для взаимодействия с сервером создается заглушка, 
	stub = iiot_device_pb2_grpc.IotDeviceStub(channel)
#создаем запрос на сервер с токеном авторизации
	req = iiot_device_pb2.DeviceListRequest()
	req.token = token
	return stub.getDeviceList(req, timeout = 10)

#забираем из ответа сервера ВСЕ действующие eui устройств и собираем из них список
def getAllEuiList(devices):
	euiList = [] # - этот список
	for i in devices:
		euiList.append(str(i.dev_eui))
	return euiList
#Создаем массив с eui датчиков из конфиг файла для запроса последниз данных с конкретных датчиков
def getEuiFromConfig():
	euiList = []
	for econs_name in getConfigData():
		euiList.append(econs_name.split(".")[0])
	
	return euiList

#получаем последнюю информации со всех датчиков, чей eui есть в euiList
def getDeviceData(euiList, channel, token):
	#по принципу протокола grpc для взаимодействия с сервером создается заглушка, относительно которой вызывает функция из прото файла
	stub = iiot_device_pb2_grpc.IotDeviceStub(channel)
	return stub.getDeviceInfo(proto(euiList, token), timeout = 10)
     
#Переводим информацию, полученную в getDeviceData
#в объекты класса MesData, где каждый объект соотвествует полной записи об одном устройстве(см.описание класса)
def toMesData(lastDataResponse):
	mesDataList = []
	configData = getConfigData()
	#Циклически создаем объекты, на основе которых будет генерироваться xml файл
	for i in lastDataResponse.body.devices:
		for j in i.sensors:
			#имя тега
			try:
				TAGName = configData[str(i.dev_eui) + '.' + str(j.sensor_id)]
			except KeyError:
				TAGName = str(i.dev_eui) + '.' + str(j.sensor_id)
			ts = j.ts.ToDatetime() + timedelta(hours = HOURS_BETWEEN_SERVERS)
			value = j.value
			mesDataList.append(md.MesData(TAGName, ts, value))
	return mesDataList

#Получаем токен авторизации от KeyCloak
def get_access_token():
	post_data_cloak = {'grant_type':"password", "client_id":"sibur-passport","username":login,"password":password}
	print(post_data_cloak)
	response = requests.post(URL_PROD_CLOAK, data = post_data_cloak, verify = False)
	return response.json()['access_token']


#Сгенерирует XML файл с последними данными ото ВСЕХ датчиков, которые есть на сервере iiot
def get_last_data_from_iiot_for_all_devices(channel, token):
	#получаем список всех устройств на сервере ИоТ
	euis = getAllEuiList(getDevices(channel, token).devices)
	#получаем последнюю информацию с этих устройств
	lastDataResponse = getDeviceData(euis, channel, token)
	#создаем объекты с информацией от датчиков(дата, имя, значение)
	mesData = toMesData(lastDataResponse)
	#генерируем xml
	toXML(mesData)



#Сгенерирует XML файл с последними данными ТОЛЬКО ДЛЯ ДАТЧИКОВ ИЗ CONFIG.INI, 
#чей dev_eui+sensor_id правильно указан
#От этой функции в 2 раза меньше запросов на сервер iiot, а 
#ответ от него ЗНАЧИТЕЛЬНО меньше, т.е. нагрузка на сервер iiot НАМНОГО НИЖЕ,
#что позволяет делать запросы чаще, чем с get_last_data_from_iiot_for_all_devices()
def get_last_data_from_iiot_for_choosen_devices(channel, token):
	euis = getEuiFromConfig()
	#получаем последнюю информацию с устройств в config.ini
	lastDataResponse = getDeviceData(euis, channel, token)
	#создаем объекты с информацией от датчиков(дата, имя, значение)
	mesData = toMesData(lastDataResponse)
	#генерируем xml
	toXML(mesData)




channel = getChannel()
token = get_access_token()


get_last_data_from_iiot_for_all_devices(channel, token)
#get_last_data_from_iiot_for_choosen_devices(channel, token)

