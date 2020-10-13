from concurrent import futures
import logging
import grpc
import iiot_device_pb2
import iiot_device_pb2_grpc
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
import mes_data as md
from mes_data import toXML
import requests
#Основной скрипт, где описаны главные функции для связи с серверами
#Здесь же происходят вызовы этих функций( в конце)


#Ввести логин и пароль
LOGIN = ''
PASSWORD = ''
URL_DEV = 'http://core.dev002.local:8080/auth-gateway/employee/log-in'
URL_TEST = 'http://siauth-tst.sibur.local:8080/employee/log-in'
URL_PROD = 'http://siauth.sibur.local:8080/employee/log-in'
IOT_IP = '127.0.0.1:7655'

#функция для аутентификации в siauth
def get_token():
	#создаем HTTP запрос с данными аутентификации
	response = request.get(URL_DEV, auth=(LOGIN, PASSWORD))
	#получаем ответ, где по пути response.data.key.token находится действующий токен 
	return response.data.key.token

#функция, собирающая объект аргумента для передачи по grpc (в соотвествии с proto файлом) 
def proto(eui, token):
	#создаем объект из автогенерированного класса
	msg = iiot_device_pb2.DeviceDataRequest()
	#выставляем поля объекта - токен и список устройств, которые сейчас подключены к ИоТ серверу (датчики)
	msg.token = token
	for i in eui:
		msg.devEuiList.append(i)
	return msg

#создаем grpc канал в соотвествии с документацией протокола
#https://grpc.io/docs/languages/python/basics/
def getChannel():
	return grpc.insecure_channel(IOT_IP)

#получаем список всех датчиков зарегестрированных на сервере ИоТ
def getDevices(channel, token):
	#по принципу протокола grpc для взаимодействия с сервером создается заглушка, относительно которой вызывает функция из прото файла
	stub = iiot_device_pb2_grpc.IotDeviceStub(channel)
	tkn = iiot_device_pb2.DeviceListRequest()
	#создаем объект из автогенерированного класса и указаываем токен
	tkn.token = token
	return stub.getDeviceList(iiot_device_pb2.DeviceListRequest(tkn))

#забираем из ответа сервера только действующие eui устройств и собираем из них список
def getEuiList(devices):
	euiList = [] # - этот список
	for i in devices:
		euiList.append(str(i.dev_eui))
	return euiList

#получаем последнюю информации со всех датчиков, для которых мы получили eui (функция getDevuces)
def getDeviceData(euiList, channel, token):
	#по принципу протокола grpc для взаимодействия с сервером создается заглушка, относительно которой вызывает функция из прото файла
	stub = iiot_device_pb2_grpc.IotDeviceStub(channel)
	return stub.getDeviceInfo(proto(euiList, token))
     
#Переводим информацию, полученную в предыдущей функции 
#в объекты класса MesData, где каждый объект соотвествует полной записи об одном устройстве(см.описание класса)
def toMesData(lastDataResponse):
	mesDataList = []
	#Циклически создаем объект, на основе которых будет генерироваться xml файл
	for i in lastDataResponse.body.devices:
		for j in i.sensors:
			TAGName = str(i.dev_eui) + '.' + str(j.sensor_id)
			ts = j.ts.ToDatetime()
			value = j.value
			mesDataList.append(md.MesData(TAGName, ts, value))
	return mesDataList


#Вызовы функций
channel = getChannel()#создаем канал для подключения по grpc
token = get_token()#получаем токен от siauth
euis = getEuiList(getDevices(channel, token).devices)#получаем список всех устройств на сервере ИоТ
lastDataResponse = getDeviceData(euis, channel, token)#получаем последнюю информацию с этих устройств
mesData = toMesData(lastDataResponse)#создаем объекты с информацией от датчиков(дата, имя, значение)
toXML(mesData)#генерируем xml





