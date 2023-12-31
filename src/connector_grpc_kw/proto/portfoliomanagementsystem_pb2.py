# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: portfoliomanagementsystem.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fportfoliomanagementsystem.proto\x12\x07packets\x1a\x19google/protobuf/any.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xd2\x01\n\x17InputPMSTransferRequest\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x16\n\x0eInstrumentCode\x18\x02 \x01(\t\x12\x12\n\nTotalUnits\x18\x03 \x01(\x01\x12\x14\n\x0cPricePerUnit\x18\x04 \x01(\x01\x12\x13\n\x0bTotalAmount\x18\x05 \x01(\x01\x12\x12\n\nCommission\x18\x06 \x01(\x01\x12\x13\n\x0bRequestType\x18\x07 \x01(\t\x12\x12\n\nSubAccount\x18\x08 \x01(\t\x12\x13\n\x0b\x46romAccount\x18\t \x01(\t\"^\n\x17OuputPMSTransferRequest\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\"\n\x04\x44\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"T\n\x17InputPMSInstrumentPrice\x12\x14\n\x0cInstrumentID\x18\x01 \x01(\x03\x12\x10\n\x08\x42uyPrice\x18\x02 \x01(\x01\x12\x11\n\tSellPrice\x18\x03 \x01(\x01\";\n\x18OutputPMSInstrumentPrice\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\"R\n\x18InputPMSTransferActivity\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x0f\n\x07Product\x18\x02 \x01(\t\x12\x15\n\rTransactionID\x18\x03 \x01(\t\"<\n\x19OutputPMSTransferActivity\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\"&\n\x14InputPMSAccountValue\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\"\\\n\x15OutputPMSAccountValue\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\"\n\x04\x44\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"&\n\x14InputPotentialProfit\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\"\xce\x01\n\x15OutputPotentialProfit\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\x15\n\rCashAllocated\x18\x03 \x01(\x01\x12\x15\n\rKoinAllocated\x18\x04 \x01(\x01\x12\x43\n\x16PotentialProfitProduct\x18\x05 \x03(\x0b\x32#.packets.PotentialProfitProductItem\x12!\n\x19PotentialProfitPercentage\x18\x06 \x01(\x01\"e\n\x1aPotentialProfitProductItem\x12\x0f\n\x07Product\x18\x01 \x01(\t\x12\x0e\n\x06\x41mount\x18\x02 \x01(\x01\x12\x12\n\nCashAmount\x18\x03 \x01(\x01\x12\x12\n\nKoinAmount\x18\x04 \x01(\x01\"\xb8\x02\n\x17InputCreateOrderHistory\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x13\n\x0bProductType\x18\x02 \x01(\t\x12\x19\n\x11TransactionStatus\x18\x03 \x01(\t\x12\x15\n\rTransactionID\x18\x04 \x01(\x03\x12\x17\n\x0fTransactionCode\x18\x05 \x01(\t\x12\x17\n\x0fTransactionDate\x18\x06 \x01(\t\x12\x14\n\x0cPurchaseType\x18\x07 \x01(\t\x12\x16\n\x0e\x41llocatedFunds\x18\x08 \x01(\x01\x12\x12\n\nTotalOrder\x18\t \x01(\x03\x12\x13\n\x0b\x41verageRate\x18\n \x01(\x01\x12\x10\n\x08Quantity\x18\x0b \x01(\x01\x12\x13\n\x0bPaymentType\x18\x0c \x01(\t\x12\x16\n\x0ePaymentChannel\x18\r \x01(\t\";\n\x18OutputCreateOrderHistory\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\"\xf2\x03\n\x17InputUpdateOrderHistory\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x13\n\x0bProductType\x18\x02 \x01(\t\x12\x15\n\rTransactionID\x18\x03 \x01(\x03\x12\x37\n\x11TransactionStatus\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0e\x41llocatedFunds\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12/\n\nTotalOrder\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x31\n\x0b\x41verageRate\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12.\n\x08Quantity\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12/\n\tExtraRate\x18\t \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x31\n\x0bPaymentType\x18\n \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0ePaymentChannel\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.StringValue\";\n\x18OutputUpdateOrderHistory\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\"\x93\x01\n\x1eInputUpdateP2POrderHistoryData\x12\x0f\n\x07OrderID\x18\x01 \x01(\x03\x12\x0f\n\x07Product\x18\x02 \x01(\t\x12\x0e\n\x06Status\x18\x03 \x01(\t\x12\x16\n\x0e\x41llocatedFunds\x18\x04 \x01(\x01\x12\x12\n\nTotalOrder\x18\x05 \x01(\x03\x12\x13\n\x0b\x41verageRate\x18\x10 \x01(\x01\"B\n\x1fOutputUpdateP2POrderHistoryData\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\"e\n\x1eOutputCurrGoldPriceAndRoboRate\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\"\n\x04\x44\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any2\xf9\x06\n\x19PortfolioManagementSystem\x12]\n\x15\x43reateTransferRequest\x12 .packets.InputPMSTransferRequest\x1a .packets.OuputPMSTransferRequest\"\x00\x12^\n\x15\x43reateInstrumentPrice\x12 .packets.InputPMSInstrumentPrice\x1a!.packets.OutputPMSInstrumentPrice\"\x00\x12\x61\n\x16\x43reateTransferActivity\x12!.packets.InputPMSTransferActivity\x1a\".packets.OutputPMSTransferActivity\"\x00\x12R\n\x0fGetAccountValue\x12\x1d.packets.InputPMSAccountValue\x1a\x1e.packets.OutputPMSAccountValue\"\x00\x12U\n\x12GetPotentialProfit\x12\x1d.packets.InputPotentialProfit\x1a\x1e.packets.OutputPotentialProfit\"\x00\x12[\n\x12\x43reateOrderHistory\x12 .packets.InputCreateOrderHistory\x1a!.packets.OutputCreateOrderHistory\"\x00\x12p\n\x19UpdateP2POrderHistoryData\x12\'.packets.InputUpdateP2POrderHistoryData\x1a(.packets.OutputUpdateP2POrderHistoryData\"\x00\x12\x63\n\x1eGetCurrentGoldPriceAndRoboRate\x12\x16.google.protobuf.Empty\x1a\'.packets.OutputCurrGoldPriceAndRoboRate\"\x00\x12[\n\x12UpdateOrderHistory\x12 .packets.InputUpdateOrderHistory\x1a!.packets.OutputUpdateOrderHistory\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'portfoliomanagementsystem_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_INPUTPMSTRANSFERREQUEST']._serialized_start=133
  _globals['_INPUTPMSTRANSFERREQUEST']._serialized_end=343
  _globals['_OUPUTPMSTRANSFERREQUEST']._serialized_start=345
  _globals['_OUPUTPMSTRANSFERREQUEST']._serialized_end=439
  _globals['_INPUTPMSINSTRUMENTPRICE']._serialized_start=441
  _globals['_INPUTPMSINSTRUMENTPRICE']._serialized_end=525
  _globals['_OUTPUTPMSINSTRUMENTPRICE']._serialized_start=527
  _globals['_OUTPUTPMSINSTRUMENTPRICE']._serialized_end=586
  _globals['_INPUTPMSTRANSFERACTIVITY']._serialized_start=588
  _globals['_INPUTPMSTRANSFERACTIVITY']._serialized_end=670
  _globals['_OUTPUTPMSTRANSFERACTIVITY']._serialized_start=672
  _globals['_OUTPUTPMSTRANSFERACTIVITY']._serialized_end=732
  _globals['_INPUTPMSACCOUNTVALUE']._serialized_start=734
  _globals['_INPUTPMSACCOUNTVALUE']._serialized_end=772
  _globals['_OUTPUTPMSACCOUNTVALUE']._serialized_start=774
  _globals['_OUTPUTPMSACCOUNTVALUE']._serialized_end=866
  _globals['_INPUTPOTENTIALPROFIT']._serialized_start=868
  _globals['_INPUTPOTENTIALPROFIT']._serialized_end=906
  _globals['_OUTPUTPOTENTIALPROFIT']._serialized_start=909
  _globals['_OUTPUTPOTENTIALPROFIT']._serialized_end=1115
  _globals['_POTENTIALPROFITPRODUCTITEM']._serialized_start=1117
  _globals['_POTENTIALPROFITPRODUCTITEM']._serialized_end=1218
  _globals['_INPUTCREATEORDERHISTORY']._serialized_start=1221
  _globals['_INPUTCREATEORDERHISTORY']._serialized_end=1533
  _globals['_OUTPUTCREATEORDERHISTORY']._serialized_start=1535
  _globals['_OUTPUTCREATEORDERHISTORY']._serialized_end=1594
  _globals['_INPUTUPDATEORDERHISTORY']._serialized_start=1597
  _globals['_INPUTUPDATEORDERHISTORY']._serialized_end=2095
  _globals['_OUTPUTUPDATEORDERHISTORY']._serialized_start=2097
  _globals['_OUTPUTUPDATEORDERHISTORY']._serialized_end=2156
  _globals['_INPUTUPDATEP2PORDERHISTORYDATA']._serialized_start=2159
  _globals['_INPUTUPDATEP2PORDERHISTORYDATA']._serialized_end=2306
  _globals['_OUTPUTUPDATEP2PORDERHISTORYDATA']._serialized_start=2308
  _globals['_OUTPUTUPDATEP2PORDERHISTORYDATA']._serialized_end=2374
  _globals['_OUTPUTCURRGOLDPRICEANDROBORATE']._serialized_start=2376
  _globals['_OUTPUTCURRGOLDPRICEANDROBORATE']._serialized_end=2477
  _globals['_PORTFOLIOMANAGEMENTSYSTEM']._serialized_start=2480
  _globals['_PORTFOLIOMANAGEMENTSYSTEM']._serialized_end=3369
# @@protoc_insertion_point(module_scope)
