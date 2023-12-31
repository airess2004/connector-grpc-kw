# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import koinrobo_pb2 as koinrobo__pb2


class KoinRoboStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOrderDetail = channel.unary_unary(
                '/packets.KoinRobo/GetOrderDetail',
                request_serializer=koinrobo__pb2.InputRoboOrderDetail.SerializeToString,
                response_deserializer=koinrobo__pb2.OutputRoboOrderDetail.FromString,
                )
        self.GetRoboUser = channel.unary_unary(
                '/packets.KoinRobo/GetRoboUser',
                request_serializer=koinrobo__pb2.InputRoboUser.SerializeToString,
                response_deserializer=koinrobo__pb2.OutputRoboUser.FromString,
                )
        self.CheckoutRoboInstant = channel.unary_unary(
                '/packets.KoinRobo/CheckoutRoboInstant',
                request_serializer=koinrobo__pb2.CheckoutRoboInstantInput.SerializeToString,
                response_deserializer=koinrobo__pb2.CheckoutRoboInstantOutput.FromString,
                )
        self.GetOrderRoboByUserID = channel.unary_unary(
                '/packets.KoinRobo/GetOrderRoboByUserID',
                request_serializer=koinrobo__pb2.InputGetOrderRoboByUserID.SerializeToString,
                response_deserializer=koinrobo__pb2.OutputGetOrderRoboByUserID.FromString,
                )
        self.GetListRoboUserID = channel.unary_unary(
                '/packets.KoinRobo/GetListRoboUserID',
                request_serializer=koinrobo__pb2.InputListRoboUserID.SerializeToString,
                response_deserializer=koinrobo__pb2.OutputListRoboUserID.FromString,
                )
        self.GetRoboBatchPerfomanceDetails = channel.unary_unary(
                '/packets.KoinRobo/GetRoboBatchPerfomanceDetails',
                request_serializer=koinrobo__pb2.InputGetRoboBatchPerfomanceDetails.SerializeToString,
                response_deserializer=koinrobo__pb2.OutputGetRoboBatchPerfomanceDetails.FromString,
                )
        self.GetRoboDailyInterest = channel.unary_unary(
                '/packets.KoinRobo/GetRoboDailyInterest',
                request_serializer=koinrobo__pb2.InputRoboDailyInterest.SerializeToString,
                response_deserializer=koinrobo__pb2.OutputRoboDailyInterest.FromString,
                )
        self.GetRoboLoanDetails = channel.unary_unary(
                '/packets.KoinRobo/GetRoboLoanDetails',
                request_serializer=koinrobo__pb2.InputRoboLoanDetails.SerializeToString,
                response_deserializer=koinrobo__pb2.OutputRoboLoanDetails.FromString,
                )
        self.GetRoboBorrowerDetailsList = channel.unary_unary(
                '/packets.KoinRobo/GetRoboBorrowerDetailsList',
                request_serializer=koinrobo__pb2.RoboBorrowerDetailsListFor.SerializeToString,
                response_deserializer=koinrobo__pb2.OutputRoboBorrowerDetailsList.FromString,
                )
        self.GetListOfFundedRobos = channel.unary_unary(
                '/packets.KoinRobo/GetListOfFundedRobos',
                request_serializer=koinrobo__pb2.InputListOfFundedRobos.SerializeToString,
                response_deserializer=koinrobo__pb2.OutputListOfFundedRobos.FromString,
                )


class KoinRoboServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetOrderDetail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRoboUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckoutRoboInstant(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrderRoboByUserID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetListRoboUserID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRoboBatchPerfomanceDetails(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRoboDailyInterest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRoboLoanDetails(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRoboBorrowerDetailsList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetListOfFundedRobos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KoinRoboServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOrderDetail': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrderDetail,
                    request_deserializer=koinrobo__pb2.InputRoboOrderDetail.FromString,
                    response_serializer=koinrobo__pb2.OutputRoboOrderDetail.SerializeToString,
            ),
            'GetRoboUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRoboUser,
                    request_deserializer=koinrobo__pb2.InputRoboUser.FromString,
                    response_serializer=koinrobo__pb2.OutputRoboUser.SerializeToString,
            ),
            'CheckoutRoboInstant': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckoutRoboInstant,
                    request_deserializer=koinrobo__pb2.CheckoutRoboInstantInput.FromString,
                    response_serializer=koinrobo__pb2.CheckoutRoboInstantOutput.SerializeToString,
            ),
            'GetOrderRoboByUserID': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrderRoboByUserID,
                    request_deserializer=koinrobo__pb2.InputGetOrderRoboByUserID.FromString,
                    response_serializer=koinrobo__pb2.OutputGetOrderRoboByUserID.SerializeToString,
            ),
            'GetListRoboUserID': grpc.unary_unary_rpc_method_handler(
                    servicer.GetListRoboUserID,
                    request_deserializer=koinrobo__pb2.InputListRoboUserID.FromString,
                    response_serializer=koinrobo__pb2.OutputListRoboUserID.SerializeToString,
            ),
            'GetRoboBatchPerfomanceDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRoboBatchPerfomanceDetails,
                    request_deserializer=koinrobo__pb2.InputGetRoboBatchPerfomanceDetails.FromString,
                    response_serializer=koinrobo__pb2.OutputGetRoboBatchPerfomanceDetails.SerializeToString,
            ),
            'GetRoboDailyInterest': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRoboDailyInterest,
                    request_deserializer=koinrobo__pb2.InputRoboDailyInterest.FromString,
                    response_serializer=koinrobo__pb2.OutputRoboDailyInterest.SerializeToString,
            ),
            'GetRoboLoanDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRoboLoanDetails,
                    request_deserializer=koinrobo__pb2.InputRoboLoanDetails.FromString,
                    response_serializer=koinrobo__pb2.OutputRoboLoanDetails.SerializeToString,
            ),
            'GetRoboBorrowerDetailsList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRoboBorrowerDetailsList,
                    request_deserializer=koinrobo__pb2.RoboBorrowerDetailsListFor.FromString,
                    response_serializer=koinrobo__pb2.OutputRoboBorrowerDetailsList.SerializeToString,
            ),
            'GetListOfFundedRobos': grpc.unary_unary_rpc_method_handler(
                    servicer.GetListOfFundedRobos,
                    request_deserializer=koinrobo__pb2.InputListOfFundedRobos.FromString,
                    response_serializer=koinrobo__pb2.OutputListOfFundedRobos.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'packets.KoinRobo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KoinRobo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetOrderDetail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinRobo/GetOrderDetail',
            koinrobo__pb2.InputRoboOrderDetail.SerializeToString,
            koinrobo__pb2.OutputRoboOrderDetail.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRoboUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinRobo/GetRoboUser',
            koinrobo__pb2.InputRoboUser.SerializeToString,
            koinrobo__pb2.OutputRoboUser.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckoutRoboInstant(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinRobo/CheckoutRoboInstant',
            koinrobo__pb2.CheckoutRoboInstantInput.SerializeToString,
            koinrobo__pb2.CheckoutRoboInstantOutput.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrderRoboByUserID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinRobo/GetOrderRoboByUserID',
            koinrobo__pb2.InputGetOrderRoboByUserID.SerializeToString,
            koinrobo__pb2.OutputGetOrderRoboByUserID.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetListRoboUserID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinRobo/GetListRoboUserID',
            koinrobo__pb2.InputListRoboUserID.SerializeToString,
            koinrobo__pb2.OutputListRoboUserID.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRoboBatchPerfomanceDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinRobo/GetRoboBatchPerfomanceDetails',
            koinrobo__pb2.InputGetRoboBatchPerfomanceDetails.SerializeToString,
            koinrobo__pb2.OutputGetRoboBatchPerfomanceDetails.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRoboDailyInterest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinRobo/GetRoboDailyInterest',
            koinrobo__pb2.InputRoboDailyInterest.SerializeToString,
            koinrobo__pb2.OutputRoboDailyInterest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRoboLoanDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinRobo/GetRoboLoanDetails',
            koinrobo__pb2.InputRoboLoanDetails.SerializeToString,
            koinrobo__pb2.OutputRoboLoanDetails.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRoboBorrowerDetailsList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinRobo/GetRoboBorrowerDetailsList',
            koinrobo__pb2.RoboBorrowerDetailsListFor.SerializeToString,
            koinrobo__pb2.OutputRoboBorrowerDetailsList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetListOfFundedRobos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinRobo/GetListOfFundedRobos',
            koinrobo__pb2.InputListOfFundedRobos.SerializeToString,
            koinrobo__pb2.OutputListOfFundedRobos.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
