# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntest.proto\x12\x07packets\x1a\x1bgoogle/protobuf/empty.proto\":\n\tBarOutput\x12\x0f\n\x07Message\x18\x01 \x01(\t\x12\x0e\n\x06Status\x18\x03 \x01(\x08\x12\x0c\n\x04\x43ode\x18\x02 \x01(\x05\x32;\n\x04Test\x12\x33\n\x03\x42\x61r\x12\x16.google.protobuf.Empty\x1a\x12.packets.BarOutput\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'test_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_BAROUTPUT']._serialized_start=52
  _globals['_BAROUTPUT']._serialized_end=110
  _globals['_TEST']._serialized_start=112
  _globals['_TEST']._serialized_end=171
# @@protoc_insertion_point(module_scope)
