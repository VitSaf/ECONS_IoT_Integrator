# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos.sibur.iiot import iiot_dimension_pb2 as protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2


class IotDimensionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getDeviceTypeList = channel.unary_unary(
                '/protos.sibur.iiot.IotDimension/getDeviceTypeList',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeviceTypeResponse.FromString,
                )
        self.getPlantList = channel.unary_unary(
                '/protos.sibur.iiot.IotDimension/getPlantList',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.PlantResponse.FromString,
                )
        self.getApplicationList = channel.unary_unary(
                '/protos.sibur.iiot.IotDimension/getApplicationList',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.ApplicationResponse.FromString,
                )
        self.getProfileList = channel.unary_unary(
                '/protos.sibur.iiot.IotDimension/getProfileList',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.ProfileResponse.FromString,
                )
        self.getPrivilegeList = channel.unary_unary(
                '/protos.sibur.iiot.IotDimension/getPrivilegeList',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.PrivilegeResponse.FromString,
                )
        self.getEventsList = channel.unary_unary(
                '/protos.sibur.iiot.IotDimension/getEventsList',
                request_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.EventsRequest.SerializeToString,
                response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.EventsResponse.FromString,
                )
        self.getMeasurementsList = channel.unary_unary(
                '/protos.sibur.iiot.IotDimension/getMeasurementsList',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.MeasurementsResponse.FromString,
                )
        self.getOrgStructure = channel.unary_unary(
                '/protos.sibur.iiot.IotDimension/getOrgStructure',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.OrgStructure.FromString,
                )
        self.listTrendGroups = channel.unary_unary(
                '/protos.sibur.iiot.IotDimension/listTrendGroups',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.TrendGroupsResponse.FromString,
                )
        self.createTrendGroup = channel.unary_unary(
                '/protos.sibur.iiot.IotDimension/createTrendGroup',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.CreateTrendGroupResponse.FromString,
                )
        self.deleteTrendGroup = channel.unary_unary(
                '/protos.sibur.iiot.IotDimension/deleteTrendGroup',
                request_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeleteTrendGroupRequest.SerializeToString,
                response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeleteTrendGroupResponse.FromString,
                )
        self.updateTrendGroup = channel.unary_unary(
                '/protos.sibur.iiot.IotDimension/updateTrendGroup',
                request_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.UpdateTrendGroupRequest.SerializeToString,
                response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.UpdateTrendGroupResponse.FromString,
                )
        self.createTrendGroupItem = channel.unary_unary(
                '/protos.sibur.iiot.IotDimension/createTrendGroupItem',
                request_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.CreateTrendGroupItemRequest.SerializeToString,
                response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.CreateTrendGroupItemResponse.FromString,
                )
        self.deleteTrendGroupItem = channel.unary_unary(
                '/protos.sibur.iiot.IotDimension/deleteTrendGroupItem',
                request_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeleteTrendGroupItemRequest.SerializeToString,
                response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeleteTrendGroupItemResponse.FromString,
                )
        self.updateTrendGroupItem = channel.unary_unary(
                '/protos.sibur.iiot.IotDimension/updateTrendGroupItem',
                request_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.UpdateTrendGroupItemRequest.SerializeToString,
                response_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.UpdateTrendGroupItemResponse.FromString,
                )


class IotDimensionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getDeviceTypeList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getPlantList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getApplicationList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getProfileList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getPrivilegeList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getEventsList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMeasurementsList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getOrgStructure(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listTrendGroups(self, request, context):
        """Trend groups
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createTrendGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteTrendGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateTrendGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createTrendGroupItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteTrendGroupItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateTrendGroupItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IotDimensionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getDeviceTypeList': grpc.unary_unary_rpc_method_handler(
                    servicer.getDeviceTypeList,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeviceTypeResponse.SerializeToString,
            ),
            'getPlantList': grpc.unary_unary_rpc_method_handler(
                    servicer.getPlantList,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.PlantResponse.SerializeToString,
            ),
            'getApplicationList': grpc.unary_unary_rpc_method_handler(
                    servicer.getApplicationList,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.ApplicationResponse.SerializeToString,
            ),
            'getProfileList': grpc.unary_unary_rpc_method_handler(
                    servicer.getProfileList,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.ProfileResponse.SerializeToString,
            ),
            'getPrivilegeList': grpc.unary_unary_rpc_method_handler(
                    servicer.getPrivilegeList,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.PrivilegeResponse.SerializeToString,
            ),
            'getEventsList': grpc.unary_unary_rpc_method_handler(
                    servicer.getEventsList,
                    request_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.EventsRequest.FromString,
                    response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.EventsResponse.SerializeToString,
            ),
            'getMeasurementsList': grpc.unary_unary_rpc_method_handler(
                    servicer.getMeasurementsList,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.MeasurementsResponse.SerializeToString,
            ),
            'getOrgStructure': grpc.unary_unary_rpc_method_handler(
                    servicer.getOrgStructure,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.OrgStructure.SerializeToString,
            ),
            'listTrendGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.listTrendGroups,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.TrendGroupsResponse.SerializeToString,
            ),
            'createTrendGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.createTrendGroup,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.CreateTrendGroupResponse.SerializeToString,
            ),
            'deleteTrendGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteTrendGroup,
                    request_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeleteTrendGroupRequest.FromString,
                    response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeleteTrendGroupResponse.SerializeToString,
            ),
            'updateTrendGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.updateTrendGroup,
                    request_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.UpdateTrendGroupRequest.FromString,
                    response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.UpdateTrendGroupResponse.SerializeToString,
            ),
            'createTrendGroupItem': grpc.unary_unary_rpc_method_handler(
                    servicer.createTrendGroupItem,
                    request_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.CreateTrendGroupItemRequest.FromString,
                    response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.CreateTrendGroupItemResponse.SerializeToString,
            ),
            'deleteTrendGroupItem': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteTrendGroupItem,
                    request_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeleteTrendGroupItemRequest.FromString,
                    response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeleteTrendGroupItemResponse.SerializeToString,
            ),
            'updateTrendGroupItem': grpc.unary_unary_rpc_method_handler(
                    servicer.updateTrendGroupItem,
                    request_deserializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.UpdateTrendGroupItemRequest.FromString,
                    response_serializer=protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.UpdateTrendGroupItemResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protos.sibur.iiot.IotDimension', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IotDimension(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getDeviceTypeList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.sibur.iiot.IotDimension/getDeviceTypeList',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeviceTypeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getPlantList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.sibur.iiot.IotDimension/getPlantList',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.PlantResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getApplicationList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.sibur.iiot.IotDimension/getApplicationList',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.ApplicationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getProfileList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.sibur.iiot.IotDimension/getProfileList',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.ProfileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getPrivilegeList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.sibur.iiot.IotDimension/getPrivilegeList',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.PrivilegeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getEventsList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.sibur.iiot.IotDimension/getEventsList',
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.EventsRequest.SerializeToString,
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.EventsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMeasurementsList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.sibur.iiot.IotDimension/getMeasurementsList',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.MeasurementsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getOrgStructure(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.sibur.iiot.IotDimension/getOrgStructure',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.OrgStructure.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listTrendGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.sibur.iiot.IotDimension/listTrendGroups',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.TrendGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createTrendGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.sibur.iiot.IotDimension/createTrendGroup',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.CreateTrendGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteTrendGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.sibur.iiot.IotDimension/deleteTrendGroup',
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeleteTrendGroupRequest.SerializeToString,
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeleteTrendGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateTrendGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.sibur.iiot.IotDimension/updateTrendGroup',
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.UpdateTrendGroupRequest.SerializeToString,
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.UpdateTrendGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createTrendGroupItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.sibur.iiot.IotDimension/createTrendGroupItem',
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.CreateTrendGroupItemRequest.SerializeToString,
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.CreateTrendGroupItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteTrendGroupItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.sibur.iiot.IotDimension/deleteTrendGroupItem',
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeleteTrendGroupItemRequest.SerializeToString,
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.DeleteTrendGroupItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateTrendGroupItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.sibur.iiot.IotDimension/updateTrendGroupItem',
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.UpdateTrendGroupItemRequest.SerializeToString,
            protos_dot_sibur_dot_iiot_dot_iiot__dimension__pb2.UpdateTrendGroupItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
