# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import koinp2p_pb2 as koinp2p__pb2


class KoinP2PStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PayOrderWaitingForTransfer = channel.unary_unary(
                '/packets.KoinP2P/PayOrderWaitingForTransfer',
                request_serializer=koinp2p__pb2.InputPayOrderKoinP2P.SerializeToString,
                response_deserializer=koinp2p__pb2.OutputPayOrderKoinP2P.FromString,
                )
        self.CancelOrderByLoanID = channel.unary_unary(
                '/packets.KoinP2P/CancelOrderByLoanID',
                request_serializer=koinp2p__pb2.InputCancelOrderByLoanID.SerializeToString,
                response_deserializer=koinp2p__pb2.OutputCancelOrderByLoanID.FromString,
                )
        self.OrderAmountByLoanID = channel.unary_unary(
                '/packets.KoinP2P/OrderAmountByLoanID',
                request_serializer=koinp2p__pb2.InputOrderAmountByLoanID.SerializeToString,
                response_deserializer=koinp2p__pb2.OutputOrderAmountByLoanIDList.FromString,
                )
        self.AddToCart = channel.unary_unary(
                '/packets.KoinP2P/AddToCart',
                request_serializer=koinp2p__pb2.InputAddToCart.SerializeToString,
                response_deserializer=koinp2p__pb2.OutputAddToCart.FromString,
                )
        self.ListCartItem = channel.unary_unary(
                '/packets.KoinP2P/ListCartItem',
                request_serializer=koinp2p__pb2.InputListCartItem.SerializeToString,
                response_deserializer=koinp2p__pb2.OutputListCartItem.FromString,
                )
        self.DeleteCartItem = channel.unary_unary(
                '/packets.KoinP2P/DeleteCartItem',
                request_serializer=koinp2p__pb2.InputDeleteCartItem.SerializeToString,
                response_deserializer=koinp2p__pb2.OutputDeleteCartItem.FromString,
                )
        self.CheckoutOrder = channel.unary_unary(
                '/packets.KoinP2P/CheckoutOrder',
                request_serializer=koinp2p__pb2.InputCheckoutOrder.SerializeToString,
                response_deserializer=koinp2p__pb2.OutputCheckoutOrder.FromString,
                )
        self.SuperappAV = channel.unary_unary(
                '/packets.KoinP2P/SuperappAV',
                request_serializer=koinp2p__pb2.InputSuperappAV.SerializeToString,
                response_deserializer=koinp2p__pb2.OutputSuperappAV.FromString,
                )
        self.ListMarketplace = channel.unary_unary(
                '/packets.KoinP2P/ListMarketplace',
                request_serializer=koinp2p__pb2.InputListMarketplace.SerializeToString,
                response_deserializer=koinp2p__pb2.OutputListMarketplace.FromString,
                )
        self.GetOrderRows = channel.unary_unary(
                '/packets.KoinP2P/GetOrderRows',
                request_serializer=koinp2p__pb2.FilterOrderRows.SerializeToString,
                response_deserializer=koinp2p__pb2.OrderRows.FromString,
                )
        self.CheckoutPrefund = channel.unary_unary(
                '/packets.KoinP2P/CheckoutPrefund',
                request_serializer=koinp2p__pb2.InputCheckoutPrefund.SerializeToString,
                response_deserializer=koinp2p__pb2.OutputCheckoutOrder.FromString,
                )
        self.GetListBorrowerRobo = channel.unary_unary(
                '/packets.KoinP2P/GetListBorrowerRobo',
                request_serializer=koinp2p__pb2.InputGetListBorrowerRobo.SerializeToString,
                response_deserializer=koinp2p__pb2.OutputGetListBorrowerRobo.FromString,
                )
        self.UpdateMarketplaceExpiredAt = channel.unary_unary(
                '/packets.KoinP2P/UpdateMarketplaceExpiredAt',
                request_serializer=koinp2p__pb2.InputUpdateMarketplaceExpiredAt.SerializeToString,
                response_deserializer=koinp2p__pb2.OutputUpdateMarketplaceExpiredAt.FromString,
                )
        self.GetPrefundReleaseDate = channel.unary_unary(
                '/packets.KoinP2P/GetPrefundReleaseDate',
                request_serializer=koinp2p__pb2.InputGetPrefundReleaseDate.SerializeToString,
                response_deserializer=koinp2p__pb2.OutputGetPrefundReleaseDate.FromString,
                )


class KoinP2PServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PayOrderWaitingForTransfer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelOrderByLoanID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OrderAmountByLoanID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddToCart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCartItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCartItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckoutOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SuperappAV(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMarketplace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrderRows(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckoutPrefund(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetListBorrowerRobo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateMarketplaceExpiredAt(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPrefundReleaseDate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KoinP2PServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PayOrderWaitingForTransfer': grpc.unary_unary_rpc_method_handler(
                    servicer.PayOrderWaitingForTransfer,
                    request_deserializer=koinp2p__pb2.InputPayOrderKoinP2P.FromString,
                    response_serializer=koinp2p__pb2.OutputPayOrderKoinP2P.SerializeToString,
            ),
            'CancelOrderByLoanID': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelOrderByLoanID,
                    request_deserializer=koinp2p__pb2.InputCancelOrderByLoanID.FromString,
                    response_serializer=koinp2p__pb2.OutputCancelOrderByLoanID.SerializeToString,
            ),
            'OrderAmountByLoanID': grpc.unary_unary_rpc_method_handler(
                    servicer.OrderAmountByLoanID,
                    request_deserializer=koinp2p__pb2.InputOrderAmountByLoanID.FromString,
                    response_serializer=koinp2p__pb2.OutputOrderAmountByLoanIDList.SerializeToString,
            ),
            'AddToCart': grpc.unary_unary_rpc_method_handler(
                    servicer.AddToCart,
                    request_deserializer=koinp2p__pb2.InputAddToCart.FromString,
                    response_serializer=koinp2p__pb2.OutputAddToCart.SerializeToString,
            ),
            'ListCartItem': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCartItem,
                    request_deserializer=koinp2p__pb2.InputListCartItem.FromString,
                    response_serializer=koinp2p__pb2.OutputListCartItem.SerializeToString,
            ),
            'DeleteCartItem': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCartItem,
                    request_deserializer=koinp2p__pb2.InputDeleteCartItem.FromString,
                    response_serializer=koinp2p__pb2.OutputDeleteCartItem.SerializeToString,
            ),
            'CheckoutOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckoutOrder,
                    request_deserializer=koinp2p__pb2.InputCheckoutOrder.FromString,
                    response_serializer=koinp2p__pb2.OutputCheckoutOrder.SerializeToString,
            ),
            'SuperappAV': grpc.unary_unary_rpc_method_handler(
                    servicer.SuperappAV,
                    request_deserializer=koinp2p__pb2.InputSuperappAV.FromString,
                    response_serializer=koinp2p__pb2.OutputSuperappAV.SerializeToString,
            ),
            'ListMarketplace': grpc.unary_unary_rpc_method_handler(
                    servicer.ListMarketplace,
                    request_deserializer=koinp2p__pb2.InputListMarketplace.FromString,
                    response_serializer=koinp2p__pb2.OutputListMarketplace.SerializeToString,
            ),
            'GetOrderRows': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrderRows,
                    request_deserializer=koinp2p__pb2.FilterOrderRows.FromString,
                    response_serializer=koinp2p__pb2.OrderRows.SerializeToString,
            ),
            'CheckoutPrefund': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckoutPrefund,
                    request_deserializer=koinp2p__pb2.InputCheckoutPrefund.FromString,
                    response_serializer=koinp2p__pb2.OutputCheckoutOrder.SerializeToString,
            ),
            'GetListBorrowerRobo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetListBorrowerRobo,
                    request_deserializer=koinp2p__pb2.InputGetListBorrowerRobo.FromString,
                    response_serializer=koinp2p__pb2.OutputGetListBorrowerRobo.SerializeToString,
            ),
            'UpdateMarketplaceExpiredAt': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateMarketplaceExpiredAt,
                    request_deserializer=koinp2p__pb2.InputUpdateMarketplaceExpiredAt.FromString,
                    response_serializer=koinp2p__pb2.OutputUpdateMarketplaceExpiredAt.SerializeToString,
            ),
            'GetPrefundReleaseDate': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPrefundReleaseDate,
                    request_deserializer=koinp2p__pb2.InputGetPrefundReleaseDate.FromString,
                    response_serializer=koinp2p__pb2.OutputGetPrefundReleaseDate.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'packets.KoinP2P', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KoinP2P(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PayOrderWaitingForTransfer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinP2P/PayOrderWaitingForTransfer',
            koinp2p__pb2.InputPayOrderKoinP2P.SerializeToString,
            koinp2p__pb2.OutputPayOrderKoinP2P.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelOrderByLoanID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinP2P/CancelOrderByLoanID',
            koinp2p__pb2.InputCancelOrderByLoanID.SerializeToString,
            koinp2p__pb2.OutputCancelOrderByLoanID.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OrderAmountByLoanID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinP2P/OrderAmountByLoanID',
            koinp2p__pb2.InputOrderAmountByLoanID.SerializeToString,
            koinp2p__pb2.OutputOrderAmountByLoanIDList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddToCart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinP2P/AddToCart',
            koinp2p__pb2.InputAddToCart.SerializeToString,
            koinp2p__pb2.OutputAddToCart.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCartItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinP2P/ListCartItem',
            koinp2p__pb2.InputListCartItem.SerializeToString,
            koinp2p__pb2.OutputListCartItem.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCartItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinP2P/DeleteCartItem',
            koinp2p__pb2.InputDeleteCartItem.SerializeToString,
            koinp2p__pb2.OutputDeleteCartItem.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckoutOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinP2P/CheckoutOrder',
            koinp2p__pb2.InputCheckoutOrder.SerializeToString,
            koinp2p__pb2.OutputCheckoutOrder.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SuperappAV(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinP2P/SuperappAV',
            koinp2p__pb2.InputSuperappAV.SerializeToString,
            koinp2p__pb2.OutputSuperappAV.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListMarketplace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinP2P/ListMarketplace',
            koinp2p__pb2.InputListMarketplace.SerializeToString,
            koinp2p__pb2.OutputListMarketplace.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrderRows(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinP2P/GetOrderRows',
            koinp2p__pb2.FilterOrderRows.SerializeToString,
            koinp2p__pb2.OrderRows.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckoutPrefund(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinP2P/CheckoutPrefund',
            koinp2p__pb2.InputCheckoutPrefund.SerializeToString,
            koinp2p__pb2.OutputCheckoutOrder.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetListBorrowerRobo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinP2P/GetListBorrowerRobo',
            koinp2p__pb2.InputGetListBorrowerRobo.SerializeToString,
            koinp2p__pb2.OutputGetListBorrowerRobo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateMarketplaceExpiredAt(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinP2P/UpdateMarketplaceExpiredAt',
            koinp2p__pb2.InputUpdateMarketplaceExpiredAt.SerializeToString,
            koinp2p__pb2.OutputUpdateMarketplaceExpiredAt.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPrefundReleaseDate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packets.KoinP2P/GetPrefundReleaseDate',
            koinp2p__pb2.InputGetPrefundReleaseDate.SerializeToString,
            koinp2p__pb2.OutputGetPrefundReleaseDate.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)