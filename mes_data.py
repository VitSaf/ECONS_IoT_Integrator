from concurrent import futures
import logging
import grpc
import iiot_device_pb2
import iiot_device_pb2_grpc
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp

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

