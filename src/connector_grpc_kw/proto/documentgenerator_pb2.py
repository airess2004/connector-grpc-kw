# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: documentgenerator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x64ocumentgenerator.proto\x12\x07packets\x1a\x19google/protobuf/any.proto\"e\n\x17GenerateDocumentRequest\x12\x12\n\nTemplateID\x18\x01 \x01(\x03\x12\x12\n\nCustomName\x18\x02 \x01(\t\x12\"\n\x04\x44\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"\x80\x01\n\x18GenerateDocumentResponse\x12\n\n\x02ID\x18\x01 \x01(\x03\x12\x14\n\x0cTemplateName\x18\x02 \x01(\t\x12\x0f\n\x07Version\x18\x03 \x01(\x03\x12\x0e\n\x06Target\x18\x04 \x01(\t\x12\x10\n\x08\x46ilename\x18\x05 \x01(\t\x12\x0f\n\x07\x46ileURL\x18\x06 \x01(\t2u\n\x18MidgardDocumentGenerator\x12Y\n\x10GenerateDocument\x12 .packets.GenerateDocumentRequest\x1a!.packets.GenerateDocumentResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'documentgenerator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GENERATEDOCUMENTREQUEST']._serialized_start=63
  _globals['_GENERATEDOCUMENTREQUEST']._serialized_end=164
  _globals['_GENERATEDOCUMENTRESPONSE']._serialized_start=167
  _globals['_GENERATEDOCUMENTRESPONSE']._serialized_end=295
  _globals['_MIDGARDDOCUMENTGENERATOR']._serialized_start=297
  _globals['_MIDGARDDOCUMENTGENERATOR']._serialized_end=414
# @@protoc_insertion_point(module_scope)