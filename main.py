from concurrent import futures
import logging
import grpc
import iiot_device_pb2
import iiot_device_pb2_grpc
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
import mes_data as md
from mes_data import toXML


def proto(eui):
	msg = iiot_device_pb2.DeviceDataRequest()
	for i in eui:
		msg.devEuiList.append(i)
	return msg


def getChannel():
	return grpc.insecure_channel('127.0.0.1:7655')#Прописать IP IoT платформы

def getDevices(channel):
	stub = iiot_device_pb2_grpc.IotDeviceStub(channel)
	return stub.getDeviceList(iiot_device_pb2.DeviceListRequest())

def getEuiList(devices):
	euiList = []
	for i in devices:
		euiList.append(str(i.dev_eui))
	return euiList

def getDeviceData(euiList, channel):
	stub = iiot_device_pb2_grpc.IotDeviceStub(channel)
	return stub.getDeviceInfo(proto(euiList))
     

def toMesData(lastDataResponse):
	mesDataList = []
	for i in lastDataResponse.body.devices:
		for j in i.sensors:
			TAGName = str(i.dev_eui) + '.' + str(j.sensor_id)
			ts = j.ts.ToDatetime()
			value = j.value
			mesDataList.append(md.MesData(TAGName, ts, value))
	return mesDataList


channel = getChannel()
euis = getEuiList(getDevices(channel).devices)
lastDataResponse = getDeviceData(euis, channel)
mesData = toMesData(lastDataResponse)
toXML(mesData)

#Для тестирования xml парсера
#testData = []
#testData.append(md.MesData('1313FA534.123', '2019-04-16 14:35:00', 55))
#testData.append(md.MesData('1313123135252FA534.321', '2017-04-16 14:35:00', 75))
#testData.append(md.MesData('1313FA5FFFF34.123', '2018-04-16 14:35:00', 25.99))
#toXML(testData)




