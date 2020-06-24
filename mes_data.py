from concurrent import futures
import logging
import grpc
import iiot_device_pb2
import iiot_device_pb2_grpc
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
import xml.etree.ElementTree as xml
from xml.etree import ElementTree
from xml.dom import minidom

class MesData(object):
	
	#String TagName
	#String ts
	#double value


	def __init__(self, TAGName, ts, v):
		self.TAGName = TAGName
		self.ts = ts
		self.value = v

	def show(self):
		print("Tag name = ", self.TAGName)
		print("Timestamp = ", self.ts)
		print("Value = ", self.value)

def prettify(elem):
	rough_string = ElementTree.tostring(elem, 'utf-8')
	reparsed = minidom.parseString(rough_string)
	return reparsed.toprettyxml(indent="  ")

def toXML(mesDataObjList):
	root = xml.Element('Import')
	dataList = xml.Element('DataList')
	dataList.set('Version', '1.0.71')
	root.append(dataList)
	for i in mesDataObjList:
		tag = xml.SubElement(dataList, 'Tag')
		tag.set('Name', str(i.TAGName))
		data = xml.SubElement(tag, 'Data')
		ts = xml.SubElement(data, 'TimeStamp')
		ts.text = str(i.ts)
		v = xml.SubElement(data, 'Value')
		v.text = str(i.value)
		dataQ = xml.SubElement(data, 'DataQuality')
		dataQ.text = 'Good'
	root = prettify(root)
	file = open('test2.xml', 'w')
	file.write(root)

