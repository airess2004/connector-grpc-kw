# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: koinbisnis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10koinbisnis.proto\x12\x07packets\x1a\x19google/protobuf/any.proto\x1a\x0c\x63ommon.proto\"+\n\x19InputKoinBisnisDetailLoan\x12\x0e\n\x06LoanID\x18\x01 \x01(\x03\"J\n\x1aOutputKoinBisnisDetailLoan\x12,\n\x05\x44\x61tas\x18\x01 \x03(\x0b\x32\x1d.packets.KoinBisnisDetailLoan\"\x81\x02\n\x14KoinBisnisDetailLoan\x12\x15\n\rLoanDetailsID\x18\x01 \x01(\x03\x12\x0e\n\x06LoanID\x18\x02 \x01(\x03\x12\x13\n\x0b\x44\x65tailGroup\x18\x03 \x01(\t\x12\x12\n\nDetailName\x18\x04 \x01(\t\x12\x13\n\x0b\x44\x65tailValue\x18\x05 \x01(\t\x12\x10\n\x08IsActive\x18\x06 \x01(\x03\x12\x11\n\tCreatedBy\x18\x07 \x01(\t\x12\x11\n\tCreatedAt\x18\x08 \x01(\t\x12\x12\n\nModifiedBy\x18\t \x01(\t\x12\x12\n\nModifiedAt\x18\n \x01(\t\x12\x11\n\tDeletedBy\x18\x0b \x01(\t\x12\x11\n\tDeletedAt\x18\x0c \x01(\t\"x\n\x1aInputBatchCreateLoanDetail\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x14\n\x0cUserInCharge\x18\x02 \x01(\t\x12\x0e\n\x06loanId\x18\x03 \x01(\x03\x12$\n\x06Params\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\"-\n\x1bOutputBatchCreateLoanDetail\x12\x0e\n\x06Status\x18\x01 \x01(\x05\"\x8c\x01\n\x15InputSubmitLoanDetail\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x0e\n\x06LoanID\x18\x02 \x01(\x03\x12\x14\n\x0cUserInCharge\x18\x03 \x01(\t\x12\x0b\n\x03Now\x18\x04 \x01(\t\x12\x0e\n\x06\x41mount\x18\x05 \x01(\x01\x12\x0c\n\x04Term\x18\x06 \x01(\x05\x12\x12\n\nVendorName\x18\x07 \x01(\t\"(\n\x16OutputSubmitLoanDetail\x12\x0e\n\x06Status\x18\x01 \x01(\x05\"\x90\x01\n\x12InputKYCValidation\x12\x1a\n\x12PartnerProductCode\x18\x01 \x01(\t\x12\x16\n\x0eValidationPage\x18\x02 \x01(\t\x12\"\n\x04Meta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\"\n\x04\x44\x61ta\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\"Z\n\x13OutputKYCValidation\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\"\n\x04\x44\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"^\n\x17\x44\x65\x66\x61ultOutputKoinBisnis\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\"\n\x04\x44\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"q\n\x13InputValidateVendor\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x10\n\x08VendorID\x18\x02 \x01(\x03\x12\x14\n\x0cValidatePage\x18\x03 \x01(\t\x12\"\n\x04Meta\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\"l\n\x14OutputValidateVendor\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\x0f\n\x07IsValid\x18\x03 \x01(\x08\x12\"\n\x04\x44\x61ta\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\"F\n\x16InputGetLoanDetailList\x12\x0e\n\x06LoanID\x18\x01 \x01(\x03\x12\x0e\n\x06Groups\x18\x02 \x03(\t\x12\x0c\n\x04Keys\x18\x03 \x03(\t\"=\n\x17OutputGetLoanDetailList\x12\"\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"L\n\x18InputGetVendorDetailList\x12\x12\n\nVendorCode\x18\x01 \x01(\t\x12\x0e\n\x06Groups\x18\x02 \x03(\t\x12\x0c\n\x04Keys\x18\x03 \x03(\t\"?\n\x19OutputGetVendorDetailList\x12\"\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"B\n\x1cInputInstantApprovalCallback\x12\"\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"@\n\x1dOutputInstantApprovalCallback\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\";\n)InputGetKoinBisnisLoanApplicationByLoanID\x12\x0e\n\x06LoanID\x18\x01 \x01(\x03\x32\xbb\x07\n\nKoinBisnis\x12W\n\nDetailLoan\x12\".packets.InputKoinBisnisDetailLoan\x1a#.packets.OutputKoinBisnisDetailLoan\"\x00\x12\x64\n\x15\x42\x61tchCreateLoanDetail\x12#.packets.InputBatchCreateLoanDetail\x1a$.packets.OutputBatchCreateLoanDetail\"\x00\x12U\n\x10SubmitLoanDetail\x12\x1e.packets.InputSubmitLoanDetail\x1a\x1f.packets.OutputSubmitLoanDetail\"\x00\x12L\n\rKYCValidation\x12\x1b.packets.InputKYCValidation\x1a\x1c.packets.OutputKYCValidation\"\x00\x12\\\n\x12GetLoanInformation\x12\".packets.InputKoinBisnisDetailLoan\x1a .packets.DefaultOutputKoinBisnis\"\x00\x12O\n\x0eValidateVendor\x12\x1c.packets.InputValidateVendor\x1a\x1d.packets.OutputValidateVendor\"\x00\x12X\n\x11GetLoanDetailList\x12\x1f.packets.InputGetLoanDetailList\x1a .packets.OutputGetLoanDetailList\"\x00\x12^\n\x13GetVendorDetailList\x12!.packets.InputGetVendorDetailList\x1a\".packets.OutputGetVendorDetailList\"\x00\x12j\n\x17InstantApprovalCallback\x12%.packets.InputInstantApprovalCallback\x1a&.packets.OutputInstantApprovalCallback\"\x00\x12t\n\x1aGetLoanApplicationByLoanID\x12\x32.packets.InputGetKoinBisnisLoanApplicationByLoanID\x1a .packets.DefaultOutputKoinBisnis\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'koinbisnis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_INPUTKOINBISNISDETAILLOAN']._serialized_start=70
  _globals['_INPUTKOINBISNISDETAILLOAN']._serialized_end=113
  _globals['_OUTPUTKOINBISNISDETAILLOAN']._serialized_start=115
  _globals['_OUTPUTKOINBISNISDETAILLOAN']._serialized_end=189
  _globals['_KOINBISNISDETAILLOAN']._serialized_start=192
  _globals['_KOINBISNISDETAILLOAN']._serialized_end=449
  _globals['_INPUTBATCHCREATELOANDETAIL']._serialized_start=451
  _globals['_INPUTBATCHCREATELOANDETAIL']._serialized_end=571
  _globals['_OUTPUTBATCHCREATELOANDETAIL']._serialized_start=573
  _globals['_OUTPUTBATCHCREATELOANDETAIL']._serialized_end=618
  _globals['_INPUTSUBMITLOANDETAIL']._serialized_start=621
  _globals['_INPUTSUBMITLOANDETAIL']._serialized_end=761
  _globals['_OUTPUTSUBMITLOANDETAIL']._serialized_start=763
  _globals['_OUTPUTSUBMITLOANDETAIL']._serialized_end=803
  _globals['_INPUTKYCVALIDATION']._serialized_start=806
  _globals['_INPUTKYCVALIDATION']._serialized_end=950
  _globals['_OUTPUTKYCVALIDATION']._serialized_start=952
  _globals['_OUTPUTKYCVALIDATION']._serialized_end=1042
  _globals['_DEFAULTOUTPUTKOINBISNIS']._serialized_start=1044
  _globals['_DEFAULTOUTPUTKOINBISNIS']._serialized_end=1138
  _globals['_INPUTVALIDATEVENDOR']._serialized_start=1140
  _globals['_INPUTVALIDATEVENDOR']._serialized_end=1253
  _globals['_OUTPUTVALIDATEVENDOR']._serialized_start=1255
  _globals['_OUTPUTVALIDATEVENDOR']._serialized_end=1363
  _globals['_INPUTGETLOANDETAILLIST']._serialized_start=1365
  _globals['_INPUTGETLOANDETAILLIST']._serialized_end=1435
  _globals['_OUTPUTGETLOANDETAILLIST']._serialized_start=1437
  _globals['_OUTPUTGETLOANDETAILLIST']._serialized_end=1498
  _globals['_INPUTGETVENDORDETAILLIST']._serialized_start=1500
  _globals['_INPUTGETVENDORDETAILLIST']._serialized_end=1576
  _globals['_OUTPUTGETVENDORDETAILLIST']._serialized_start=1578
  _globals['_OUTPUTGETVENDORDETAILLIST']._serialized_end=1641
  _globals['_INPUTINSTANTAPPROVALCALLBACK']._serialized_start=1643
  _globals['_INPUTINSTANTAPPROVALCALLBACK']._serialized_end=1709
  _globals['_OUTPUTINSTANTAPPROVALCALLBACK']._serialized_start=1711
  _globals['_OUTPUTINSTANTAPPROVALCALLBACK']._serialized_end=1775
  _globals['_INPUTGETKOINBISNISLOANAPPLICATIONBYLOANID']._serialized_start=1777
  _globals['_INPUTGETKOINBISNISLOANAPPLICATIONBYLOANID']._serialized_end=1836
  _globals['_KOINBISNIS']._serialized_start=1839
  _globals['_KOINBISNIS']._serialized_end=2794
# @@protoc_insertion_point(module_scope)