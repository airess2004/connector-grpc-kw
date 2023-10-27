# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import koinbisnis_pb2 as koinbisnis__pb2


class KoinBisnisStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DetailLoan = channel.unary_unary(
                '/packets.KoinBisnis/DetailLoan',
                request_serializer=koinbisnis__pb2.InputKoinBisnisDetailLoan.SerializeToString,
                response_deserializer=koinbisnis__pb2.OutputKoinBisnisDetailLoan.FromString,
                )
        self.BatchCreateLoanDetail = channel.unary_unary(
                '/packets.KoinBisnis/BatchCreateLoanDetail',
                request_serializer=koinbisnis__pb2.InputBatchCreateLoanDetail.SerializeToString,
                response_deserializer=koinbisnis__pb2.OutputBatchCreateLoanDetail.FromString,
                )
        self.SubmitLoanDetail = channel.unary_unary(
                '/packets.KoinBisnis/SubmitLoanDetail',
                request_serializer=koinbisnis__pb2.InputSubmitLoanDetail.SerializeToString,
                response_deserializer=koinbisnis__pb2.OutputSubmitLoanDetail.FromString,
                )
        self.KYCValidation = channel.unary_unary(
                '/packets.KoinBisnis/KYCValidation',
                request_serializer=koinbisnis__pb2.InputKYCValidation.SerializeToString,
                response_deserializer=koinbisnis__pb2.OutputKYCValidation.FromString,
                )
        self.GetLoanInformation = channel.unary_unary(
                '/packets.KoinBisnis/GetLoanInformation',
                request_serializer=koinbisnis__pb2.InputKoinBisnisDetailLoan.SerializeToString,
                response_deserializer=koinbisnis__pb2.DefaultOutputKoinBisnis.FromString,
                )
        self.ValidateVendor = channel.unary_unary(
                '/packets.KoinBisnis/ValidateVendor',
                request_serializer=koinbisnis__pb2.InputValidateVendor.SerializeToString,
                response_deserializer=koinbisnis__pb2.OutputValidateVendor.FromString,
                )
        self.GetLoanDetailList = channel.unary_unary(
                '/packets.KoinBisnis/GetLoanDetailList',
                request_serializer=koinbisnis__pb2.InputGetLoanDetailList.SerializeToString,
                response_deserializer=koinbisnis__pb2.OutputGetLoanDetailList.FromString,
                )
        self.GetVendorDetailList = channel.unary_unary(
                '/packets.KoinBisnis/GetVendorDetailList',
                request_serializer=koinbisnis__pb2.InputGetVendorDetailList.SerializeToString,
                response_deserializer=koinbisnis__pb2.OutputGetVendorDetailList.FromString,
                )
        self.InstantApprovalCallback = channel.unary_unary(
                '/packets.KoinBisnis/InstantApprovalCallback',
                request_serializer=koinbisnis__pb2.InputInstantApprovalCallback.SerializeToString,
                response_deserializer=koinbisnis__pb2.OutputInstantApprovalCallback.FromString,
                )
        self.GetLoanApplicationByLoanID = channel.unary_unary(
                '/packets.KoinBisnis/GetLoanApplicationByLoanID',
                request_serializer=koinbisnis__pb2.InputGetKoinBisnisLoanApplicationByLoanID.SerializeToString,
                response_deserializer=koinbisnis__pb2.DefaultOutputKoinBisnis.FromString,
                )


class KoinBisnisServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DetailLoan(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchCreateLoanDetail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitLoanDetail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def KYCValidation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLoanInformation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidateVendor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLoanDetailList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVendorDetailList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InstantApprovalCallback(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLoanApplicationByLoanID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KoinBisnisServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DetailLoan': grpc.unary_unary_rpc_method_handler(
                    servicer.DetailLoan,
                    request_deserializer=koinbisnis__pb2.InputKoinBisnisDetailLoan.FromString,
                    response_serializer=koinbisnis__pb2.OutputKoinBisnisDetailLoan.SerializeToString,
            ),
            'BatchCreateLoanDetail': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchCreateLoanDetail,
                    request_deserializer=koinbisnis__pb2.InputBatchCreateLoanDetail.FromString,
                    response_serializer=koinbisnis__pb2.OutputBatchCreateLoanDetail.SerializeToString,
            ),
            'SubmitLoanDetail': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitLoanDetail,
                    request_deserializer=koinbisnis__pb2.InputSubmitLoanDetail.FromString,
                    response_serializer=koinbisnis__pb2.OutputSubmitLoanDetail.SerializeToString,
            ),
            'KYCValidation': grpc.unary_unary_rpc_method_handler(
                    servicer.KYCValidation,
                    request_deserializer=koinbisnis__pb2.InputKYCValidation.FromString,
                    response_serializer=koinbisnis__pb2.OutputKYCValidation.SerializeToString,
            ),
            'GetLoanInformation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLoanInformation,
                    request_deserializer=koinbisnis__pb2.InputKoinBisnisDetailLoan.FromString,
                    response_serializer=koinbisnis__pb2.DefaultOutputKoinBisnis.SerializeToString,
            ),
            'ValidateVendor': grpc.unary_unary_rpc_method_handler(
                    servicer.ValidateVendor,
                    request_deserializer=koinbisnis__pb2.InputValidateVendor.FromString,
                    response_serializer=koinbisnis__pb2.OutputValidateVendor.SerializeToString,
            ),
            'GetLoanDetailList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLoanDetailList,
                    request_deserializer=koinbisnis__pb2.InputGetLoanDetailList.FromString,
                    response_serializer=koinbisnis__pb2.OutputGetLoanDetailList.SerializeToString,
            ),
            'GetVendorDetailList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVendorDetailList,
                    request_deserializer=koinbisnis__pb2.InputGetVendorDetailList.FromString,
                    response_serializer=koinbisnis__pb2.OutputGetVendorDetailList.SerializeToString,
            ),
            'InstantApprovalCallback': grpc.unary_unary_rpc_method_handler(
                    servicer.InstantApprovalCallback,
                    request_deserializer=koinbisnis__pb2.InputInstantApprovalCallback.FromString,
                    response_serializer=koinbisnis__pb2.OutputInstantApprovalCallback.SerializeToString,
            ),
            'GetLoanApplicationByLoanID': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLoanApplicationByLoanID,
                    request_deserializer=koinbisnis__pb2.InputGetKoinBisnisLoanApplicationByLoanID.FromString,
                    response_serializer=koinbisnis__pb2.DefaultOutputKoinBisnis.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'packets.KoinBisnis', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KoinBisnis(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DetailLoan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinBisnis/DetailLoan',
            koinbisnis__pb2.InputKoinBisnisDetailLoan.SerializeToString,
            koinbisnis__pb2.OutputKoinBisnisDetailLoan.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchCreateLoanDetail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinBisnis/BatchCreateLoanDetail',
            koinbisnis__pb2.InputBatchCreateLoanDetail.SerializeToString,
            koinbisnis__pb2.OutputBatchCreateLoanDetail.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubmitLoanDetail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinBisnis/SubmitLoanDetail',
            koinbisnis__pb2.InputSubmitLoanDetail.SerializeToString,
            koinbisnis__pb2.OutputSubmitLoanDetail.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def KYCValidation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinBisnis/KYCValidation',
            koinbisnis__pb2.InputKYCValidation.SerializeToString,
            koinbisnis__pb2.OutputKYCValidation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLoanInformation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinBisnis/GetLoanInformation',
            koinbisnis__pb2.InputKoinBisnisDetailLoan.SerializeToString,
            koinbisnis__pb2.DefaultOutputKoinBisnis.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValidateVendor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinBisnis/ValidateVendor',
            koinbisnis__pb2.InputValidateVendor.SerializeToString,
            koinbisnis__pb2.OutputValidateVendor.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLoanDetailList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinBisnis/GetLoanDetailList',
            koinbisnis__pb2.InputGetLoanDetailList.SerializeToString,
            koinbisnis__pb2.OutputGetLoanDetailList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVendorDetailList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinBisnis/GetVendorDetailList',
            koinbisnis__pb2.InputGetVendorDetailList.SerializeToString,
            koinbisnis__pb2.OutputGetVendorDetailList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InstantApprovalCallback(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinBisnis/InstantApprovalCallback',
            koinbisnis__pb2.InputInstantApprovalCallback.SerializeToString,
            koinbisnis__pb2.OutputInstantApprovalCallback.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLoanApplicationByLoanID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinBisnis/GetLoanApplicationByLoanID',
            koinbisnis__pb2.InputGetKoinBisnisLoanApplicationByLoanID.SerializeToString,
            koinbisnis__pb2.DefaultOutputKoinBisnis.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
