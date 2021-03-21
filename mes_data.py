from concurrent import futures
import logging
import grpc
import iiot_device_pb2
import iiot_device_pb2_grpc
from datetime import datetime, timedelta
from google.protobuf.timestamp_pb2 import Timestamp
import xml.etree.ElementTree as xml
from xml.etree import ElementTree
from xml.dom import minidom
import configparser

#откидываем данные старше, чем столько дней
DAYS_WITHOUT_UPD = 7
#Путь до файл ридера historian'a
SAVE_XML_PATH = 'F:\\Proficy Historian Data\\ImportFiles\\Incoming\\iot_last_data.xml'
print(DAYS_WITHOUT_UPD)

#Класс для инкапсуляции данных
class MesData(object):
    #Конструктор класса
    def __init__(self, TAGName, ts, v):
        self.TAGName = TAGName
        self.ts = ts
        self.value = v
#преобразует xml файл к читабельному человеком виду
#(красивая разметка)    
def prettify(elem):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

#возращает данные секции DEFAULT из конфиг файла, где описано соответствие имен iiot сервера
#именам сервера эконс
def getConfigData():
    config = configparser.ConfigParser()
    config.read('settings.ini', encoding='utf-8-sig')
    return config['DEFAULT']

        

#функция, генерирующая xml файл
#в теле функции задается структура файла, версия и содержимое
#Всё это определялось требованиями сервера ЭКОНС
#т.к он читает только xml файлы строго определенной иерархии
def toXML(mesDataObjList):
    configData = getConfigData()
    root = xml.Element('Import')
    dataList = xml.Element('DataList')
    dataList.set('Version', '1.0.71')
    root.append(dataList)
    for i in mesDataObjList:
        #Если датчик не присылал данные последние DAYS_WITHOUT_UPD дней, то выкидываем их
                if i.ts < (datetime.now() - timedelta(days = DAYS_WITHOUT_UPD)):
                    continue
                econs_name = find_name(str(i.TAGName), configData)
                tag = xml.SubElement(dataList, 'Tag')
                tag.set('Name', econs_name)
                data = xml.SubElement(tag, 'Data')
                ts = xml.SubElement(data, 'TimeStamp')
                ts.text = str(i.ts)
                v = xml.SubElement(data, 'Value')
                try:
                    val = str(i.value).split(' ')[1]
                    print(type(i.value), val)
                    v.text = val
                except:
                    continue
                dataQ = xml.SubElement(data, 'DataQuality')
                dataQ.text = 'Good'
    root = prettify(root)
    try:
        file = open(SAVE_XML_PATH, 'w')
    except:
        file = open('test.xml', 'w')
    file.write(root)

