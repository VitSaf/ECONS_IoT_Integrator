from concurrent import futures
import logging
import grpc
import protos.sibur.iiot.iiot_device_pb2 as iiot_device_pb2
import protos.sibur.iiot.iiot_device_pb2_grpc as iiot_device_pb2_grpc
from datetime import datetime,timedelta
from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.empty_pb2 import Empty
import mes_data as md
from mes_data import toXML, getConfigData
import configparser
import requests


#Основной скрипт, где описаны главные функции для связи с серверами
#Здесь же происходят вызовы этих функций( в конце)

#сервер iiot
PROD_IOT_IP = '10.81.198.163:7655'
PROD_LOGIN = '""'
PROD_PASSWORD = '""'
#сервер аутентификации
URL_DEV_CLOAK = 'https://s001dp-0093.dev002.local/auth/realms/sibur/protocol/openid-connect/token'
URL_PROD_SIAUTH_IIOT = 'https://vsk.iot.sibur.local/siauth/employee/log-in'
URL_PROD_CLOAK = 'https://keycloak.sibur.local/auth/realms/sibur/protocol/openid-connect/token'
#разница между временем сервера iiot и "ЭКОНС"(сколько часов добавить ко времени, полученному с iiot)
HOURS_BETWEEN_SERVERS = 3

#Для аутентификации


DEV_SIAUTH = 'core.dev002.local:8080/auth-gateway/employee/log-in'
DEV_SIAUTH_IIOT = 'https://s001i4-0018/siauth/employee/log-in'
DEV_IIOT = '172.21.4.107:7654'
dev_login = '""' 
dev_password = '""'


#функция, собирающая объект для передачи по grpc (в соотвествии с proto файлом) с инфо по датчикам,
#данные для которых мы запрашиваем
def proto(euis):
	#создаем объект из автогенерированного класса
	msg = iiot_device_pb2.DeviceDataRequest()
	#выставляем поля объекта - токен и список устройств, которые сейчас подключены к ИоТ серверу (датчики)
	for i in euis:
		msg.devEuiList.append(i)
	return msg

#Получаем токен авторизации от KeyCloak
def get_keycloak_token(login, password, url):
	post_data_cloak = {'grant_type':"password", "client_id":"sibur-passport","username":login,"password":password}
	print(post_data_cloak)
	response = requests.post(url, data = post_data_cloak, verify = False)
	return response.json()['access_token']

def get_siauth_token(login, password, url):
	post_data = '{"basic_authentication":{"login":'+ login +',"password":'+password+'}}'
	response = requests.post(url, data = post_data, verify = False)
	return response.json()['data']['key']['token']

#создаем grpc канал в соотвествии с документацией протокола
#https://grpc.io/docs/languages/python/basics/
def getChannel(ip):
	return grpc.insecure_channel(ip)

#получаем список всех датчиков зарегестрированных на сервере ИоТ
def getDevices(channel, token):
#по принципу протокола grpc для взаимодействия с сервером создается заглушка, 
	stub = iiot_device_pb2_grpc.IotDeviceStub(channel)
	metadata = (('x-auth-token',token),)
	return stub.getDeviceList(request = Empty(), metadata = metadata, timeout = 10)

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
	metadata = (('x-auth-token',token),)
	return stub.getDeviceInfo(proto(euiList), metadata = metadata, timeout = 10)
     
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




channel = getChannel(PROD_IOT_IP)

token = get_siauth_token(PROD_LOGIN, PROD_PASSWORD, URL_PROD_SIAUTH_IIOT)
#token = get_keycloak_token(PROD_LOGIN.replace('"',''), PROD_PASSWORD.replace('"',''), URL_PROD_CLOAK)


get_last_data_from_iiot_for_all_devices(channel, token)
#get_last_data_from_iiot_for_choosen_devices(channel, token)


