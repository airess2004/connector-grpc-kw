# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: koinpintar.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10koinpintar.proto\x12\x07packets\x1a\x19google/protobuf/any.proto\"+\n\x19InputKoinPintarDetailLoan\x12\x0e\n\x06LoanID\x18\x01 \x01(\x03\"J\n\x1aOutputKoinPintarDetailLoan\x12,\n\x05\x44\x61tas\x18\x01 \x03(\x0b\x32\x1d.packets.KoinPintarDetailLoan\"\x81\x02\n\x14KoinPintarDetailLoan\x12\x15\n\rLoanDetailsID\x18\x01 \x01(\x03\x12\x0e\n\x06LoanID\x18\x02 \x01(\x03\x12\x13\n\x0b\x44\x65tailGroup\x18\x03 \x01(\t\x12\x12\n\nDetailName\x18\x04 \x01(\t\x12\x13\n\x0b\x44\x65tailValue\x18\x05 \x01(\t\x12\x10\n\x08IsActive\x18\x06 \x01(\x03\x12\x11\n\tCreatedBy\x18\x07 \x01(\t\x12\x11\n\tCreatedAt\x18\x08 \x01(\t\x12\x12\n\nModifiedBy\x18\t \x01(\t\x12\x12\n\nModifiedAt\x18\n \x01(\t\x12\x11\n\tDeletedBy\x18\x0b \x01(\t\x12\x11\n\tDeletedAt\x18\x0c \x01(\t\"_\n\x18\x44\x65\x66\x61ultOutputKoinPintars\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\"\n\x04\x44\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any2\xae\x02\n\x0bKoinPintars\x12W\n\nDetailLoan\x12\".packets.InputKoinPintarDetailLoan\x1a#.packets.OutputKoinPintarDetailLoan\"\x00\x12g\n\x1aGetKoinPintarPartnerByLoan\x12\".packets.InputKoinPintarDetailLoan\x1a#.packets.OutputKoinPintarDetailLoan\"\x00\x12]\n\x12GetLoanInformation\x12\".packets.InputKoinPintarDetailLoan\x1a!.packets.DefaultOutputKoinPintars\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'koinpintar_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_INPUTKOINPINTARDETAILLOAN']._serialized_start=56
  _globals['_INPUTKOINPINTARDETAILLOAN']._serialized_end=99
  _globals['_OUTPUTKOINPINTARDETAILLOAN']._serialized_start=101
  _globals['_OUTPUTKOINPINTARDETAILLOAN']._serialized_end=175
  _globals['_KOINPINTARDETAILLOAN']._serialized_start=178
  _globals['_KOINPINTARDETAILLOAN']._serialized_end=435
  _globals['_DEFAULTOUTPUTKOINPINTARS']._serialized_start=437
  _globals['_DEFAULTOUTPUTKOINPINTARS']._serialized_end=532
  _globals['_KOINPINTARS']._serialized_start=535
  _globals['_KOINPINTARS']._serialized_end=837
# @@protoc_insertion_point(module_scope)
