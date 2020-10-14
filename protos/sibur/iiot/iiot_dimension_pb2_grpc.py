# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from protos.sibur.iiot import iiot_dimension_pb2 as protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2


class IotDimensionStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getDeviceTypeList = channel.unary_unary(
        '/protos.sibur.iiot.IotDimension/getDeviceTypeList',
        request_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeviceTypeRequest.SerializeToString,
        response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeviceTypeResponse.FromString,
        )
    self.getPlantList = channel.unary_unary(
        '/protos.sibur.iiot.IotDimension/getPlantList',
        request_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.PlantRequest.SerializeToString,
        response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.PlantResponse.FromString,
        )
    self.getApplicationList = channel.unary_unary(
        '/protos.sibur.iiot.IotDimension/getApplicationList',
        request_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.ApplicationRequest.SerializeToString,
        response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.ApplicationResponse.FromString,
        )
    self.getProfileList = channel.unary_unary(
        '/protos.sibur.iiot.IotDimension/getProfileList',
        request_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.ProfileRequest.SerializeToString,
        response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.ProfileResponse.FromString,
        )
    self.getPrivilegeList = channel.unary_unary(
        '/protos.sibur.iiot.IotDimension/getPrivilegeList',
        request_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.PrivilegeRequest.SerializeToString,
        response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.PrivilegeResponse.FromString,
        )


class IotDimensionServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def getDeviceTypeList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getPlantList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getApplicationList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getProfileList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getPrivilegeList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IotDimensionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getDeviceTypeList': grpc.unary_unary_rpc_method_handler(
          servicer.getDeviceTypeList,
          request_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeviceTypeRequest.FromString,
          response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeviceTypeResponse.SerializeToString,
      ),
      'getPlantList': grpc.unary_unary_rpc_method_handler(
          servicer.getPlantList,
          request_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.PlantRequest.FromString,
          response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.PlantResponse.SerializeToString,
      ),
      'getApplicationList': grpc.unary_unary_rpc_method_handler(
          servicer.getApplicationList,
          request_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.ApplicationRequest.FromString,
          response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.ApplicationResponse.SerializeToString,
      ),
      'getProfileList': grpc.unary_unary_rpc_method_handler(
          servicer.getProfileList,
          request_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.ProfileRequest.FromString,
          response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.ProfileResponse.SerializeToString,
      ),
      'getPrivilegeList': grpc.unary_unary_rpc_method_handler(
          servicer.getPrivilegeList,
          request_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.PrivilegeRequest.FromString,
          response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.PrivilegeResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'protos.sibur.iiot.IotDimension', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))