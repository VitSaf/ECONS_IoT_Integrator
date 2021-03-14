from concurrent import futures
import logging
import grpc
import iiot_device_pb2
import iiot_device_pb2_grpc
from datetime import datetime,timedelta
from google.protobuf.timestamp_pb2 import Timestamp
import mes_data as md
from mes_data import toXML

#Основной скрипт, где описаны главные функции для связи с серверами
#Здесь же происходят вызовы этих функций( в конце)


#Ввести логин и пароль
IOT_IP = ""
URL_PROD_CLOAK = ""
HOURS_TO_VRN_TIME = 3

login = ""
password = ""


#функция, собирающая объект аргумента для передачи по grpc (в соотвествии с proto файлом) 
def proto(eui, token):
	#создаем объект из автогенерированного класса
	msg = iiot_device_pb2.DeviceDataRequest()
	msg.token = token
	#выставляем поля объекта - токен и список устройств, которые сейчас подключены к ИоТ серверу (датчики)
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
	req = iiot_device_pb2.DeviceListRequest()
	req.token = token
	return stub.getDeviceList(req, timeout = 10)

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
	#Циклически создаем объекты, на основе которых будет генерироваться xml файл
	for i in lastDataResponse.body.devices:
		for j in i.sensors:
			TAGName = str(i.dev_eui) + '.' + str(j.sensor_id)
			ts = j.ts.ToDatetime() + timedelta(hours = HOURS_TO_VRN_TIME)
			value = j.value
			mesDataList.append(md.MesData(TAGName, ts, value))
	return mesDataList

def get_access_token():
	post_data_cloak = {'grant_type':"password", "client_id":"sibur-passport","username":login,"password":password}
	print(post_data_cloak)
	response = requests.post(URL_PROD_CLOAK, data = post_data_cloak, verify = False)
	return response.json()['access_token']

#Вызовы функций
channel = getChannel()#создаем канал для подключения по grpc
token = get_access_token()
euis = getEuiList(getDevices(channel, token).devices)#получаем список всех устройств на сервере ИоТ
print(euis)
lastDataResponse = getDeviceData(euis, channel, token)#получаем последнюю информацию с этих устройств
mesData = toMesData(lastDataResponse)#создаем объекты с информацией от датчиков(дата, имя, значение)
toXML(mesData)#генерируем xml







