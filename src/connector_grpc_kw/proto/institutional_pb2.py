# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: institutional.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13institutional.proto\x12\x07packets\"&\n\x14InputGetLoanCriteria\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\"\xb9\x01\n\x15OutputGetLoanCriteria\x12\r\n\x05Grade\x18\x01 \x01(\t\x12\x0f\n\x07MinRate\x18\x02 \x01(\x01\x12\x0f\n\x07MaxRate\x18\x03 \x01(\x01\x12\x11\n\tMinAmount\x18\x04 \x01(\x01\x12\x11\n\tMaxAmount\x18\x05 \x01(\x01\x12\x11\n\tMinTenure\x18\x06 \x01(\x03\x12\x11\n\tMaxTenure\x18\x07 \x01(\x03\x12\x0f\n\x07Product\x18\x08 \x01(\t\x12\x12\n\nBorrowerID\x18\t \x01(\t\"C\n!InputUpdatePrefundExecutionStatus\x12\x0e\n\x06LoanId\x18\x01 \x01(\x03\x12\x0e\n\x06Status\x18\x02 \x01(\t\"E\n\"OutputUpdatePrefundExecutionStatus\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t2\xe7\x01\n\rInstitutional\x12R\n\x0fGetLoanCriteria\x12\x1d.packets.InputGetLoanCriteria\x1a\x1e.packets.OutputGetLoanCriteria\"\x00\x12\x81\x01\n$UpdatePrefundExecutionStatusByLoanId\x12*.packets.InputUpdatePrefundExecutionStatus\x1a+.packets.OutputUpdatePrefundExecutionStatus\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'institutional_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_INPUTGETLOANCRITERIA']._serialized_start=32
  _globals['_INPUTGETLOANCRITERIA']._serialized_end=70
  _globals['_OUTPUTGETLOANCRITERIA']._serialized_start=73
  _globals['_OUTPUTGETLOANCRITERIA']._serialized_end=258
  _globals['_INPUTUPDATEPREFUNDEXECUTIONSTATUS']._serialized_start=260
  _globals['_INPUTUPDATEPREFUNDEXECUTIONSTATUS']._serialized_end=327
  _globals['_OUTPUTUPDATEPREFUNDEXECUTIONSTATUS']._serialized_start=329
  _globals['_OUTPUTUPDATEPREFUNDEXECUTIONSTATUS']._serialized_end=398
  _globals['_INSTITUTIONAL']._serialized_start=401
  _globals['_INSTITUTIONAL']._serialized_end=632
# @@protoc_insertion_point(module_scope)