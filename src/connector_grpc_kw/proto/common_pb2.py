# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63ommon.proto\x12\x07packets\"%\n\x07PObject\x12\x0c\n\x04Type\x18\x01 \x01(\t\x12\x0c\n\x04\x42ody\x18\x02 \x01(\x0c\"\xf5\x01\n\x0ePViewArguments\x12\x11\n\tProcessID\x18\x07 \x01(\t\x12\x0e\n\x06Offset\x18\x01 \x01(\x03\x12\r\n\x05Limit\x18\x02 \x01(\x05\x12\x0f\n\x07Sorting\x18\x03 \x03(\t\x12;\n\nConditions\x18\x04 \x03(\x0b\x32\'.packets.PViewArguments.ConditionsEntry\x12\x0e\n\x06\x46ields\x18\x05 \x03(\t\x12\x0e\n\x06Groups\x18\x06 \x03(\t\x1a\x43\n\x0f\x43onditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.packets.PObject:\x02\x38\x01\"W\n\x06PError\x12\x0c\n\x04\x43ode\x18\x01 \x01(\x05\x12\x0b\n\x03Key\x18\x02 \x01(\t\x12\x0f\n\x07Message\x18\x03 \x01(\t\x12\x0f\n\x07\x43omment\x18\x04 \x01(\t\x12\x10\n\x08MoreInfo\x18\x05 \x01(\t\";\n\x07PStatus\x12\x0f\n\x07Success\x18\x01 \x01(\x08\x12\x1f\n\x06\x45rrors\x18\x02 \x03(\x0b\x32\x0f.packets.PError\"n\n\x0ePViewAttribute\x12\n\n\x02ID\x18\x01 \x01(\x03\x12\x0b\n\x03Key\x18\x02 \x01(\t\x12\r\n\x05Group\x18\x03 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x04 \x01(\t\x12\x1f\n\x05Value\x18\x05 \x01(\x0b\x32\x10.packets.PObject\"H\n\tPViewData\x12\x0e\n\x06\x46ields\x18\x01 \x03(\t\x12+\n\nAttributes\x18\x02 \x03(\x0b\x32\x17.packets.PViewAttribute\"<\n\nPInputData\x12\n\n\x02ID\x18\x01 \x01(\x03\x12\x13\n\x0b\x44\x65scription\x18\x02 \x01(\t\x12\r\n\x05Value\x18\x03 \x01(\t\"Q\n\rPInputAnyData\x12\n\n\x02ID\x18\x01 \x01(\x03\x12\x13\n\x0b\x44\x65scription\x18\x02 \x01(\t\x12\x1f\n\x05Value\x18\x03 \x01(\x0b\x32\x10.packets.PObject\"U\n\x0ePViewResponses\x12 \n\x06Status\x18\x01 \x01(\x0b\x32\x10.packets.PStatus\x12!\n\x05\x44\x61tas\x18\x02 \x03(\x0b\x32\x12.packets.PViewData\"\xa1\x03\n\x0fPInputArguments\x12\x11\n\tProcessID\x18\x04 \x01(\t\x12<\n\nConditions\x18\x01 \x03(\x0b\x32(.packets.PInputArguments.ConditionsEntry\x12<\n\nAttributes\x18\x02 \x03(\x0b\x32(.packets.PInputArguments.AttributesEntry\x12\x32\n\x05Metas\x18\x03 \x03(\x0b\x32#.packets.PInputArguments.MetasEntry\x1a\x43\n\x0f\x43onditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.packets.PObject:\x02\x38\x01\x1a\x43\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.packets.PObject:\x02\x38\x01\x1a\x41\n\nMetasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.packets.PInputData:\x02\x38\x01\"\xc0\x01\n\x10PUpdateResponses\x12 \n\x06Status\x18\x01 \x01(\x0b\x32\x10.packets.PStatus\x12\x15\n\rAffectedCount\x18\x02 \x01(\x03\x12?\n\x0b\x41\x66\x66\x65\x63tedIDs\x18\x03 \x03(\x0b\x32*.packets.PUpdateResponses.AffectedIDsEntry\x1a\x32\n\x10\x41\x66\x66\x65\x63tedIDsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"\x8d\x02\n\x10PInsertResponses\x12 \n\x06Status\x18\x01 \x01(\x0b\x32\x10.packets.PStatus\x12/\n\x03IDs\x18\x02 \x03(\x0b\x32\".packets.PInsertResponses.IDsEntry\x12\x33\n\x05Metas\x18\x03 \x03(\x0b\x32$.packets.PInsertResponses.MetasEntry\x1a*\n\x08IDsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x45\n\nMetasEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.packets.PViewResponses:\x02\x38\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _PVIEWARGUMENTS_CONDITIONSENTRY._options = None
  _PVIEWARGUMENTS_CONDITIONSENTRY._serialized_options = b'8\001'
  _PINPUTARGUMENTS_CONDITIONSENTRY._options = None
  _PINPUTARGUMENTS_CONDITIONSENTRY._serialized_options = b'8\001'
  _PINPUTARGUMENTS_ATTRIBUTESENTRY._options = None
  _PINPUTARGUMENTS_ATTRIBUTESENTRY._serialized_options = b'8\001'
  _PINPUTARGUMENTS_METASENTRY._options = None
  _PINPUTARGUMENTS_METASENTRY._serialized_options = b'8\001'
  _PUPDATERESPONSES_AFFECTEDIDSENTRY._options = None
  _PUPDATERESPONSES_AFFECTEDIDSENTRY._serialized_options = b'8\001'
  _PINSERTRESPONSES_IDSENTRY._options = None
  _PINSERTRESPONSES_IDSENTRY._serialized_options = b'8\001'
  _PINSERTRESPONSES_METASENTRY._options = None
  _PINSERTRESPONSES_METASENTRY._serialized_options = b'8\001'
  _globals['_POBJECT']._serialized_start=25
  _globals['_POBJECT']._serialized_end=62
  _globals['_PVIEWARGUMENTS']._serialized_start=65
  _globals['_PVIEWARGUMENTS']._serialized_end=310
  _globals['_PVIEWARGUMENTS_CONDITIONSENTRY']._serialized_start=243
  _globals['_PVIEWARGUMENTS_CONDITIONSENTRY']._serialized_end=310
  _globals['_PERROR']._serialized_start=312
  _globals['_PERROR']._serialized_end=399
  _globals['_PSTATUS']._serialized_start=401
  _globals['_PSTATUS']._serialized_end=460
  _globals['_PVIEWATTRIBUTE']._serialized_start=462
  _globals['_PVIEWATTRIBUTE']._serialized_end=572
  _globals['_PVIEWDATA']._serialized_start=574
  _globals['_PVIEWDATA']._serialized_end=646
  _globals['_PINPUTDATA']._serialized_start=648
  _globals['_PINPUTDATA']._serialized_end=708
  _globals['_PINPUTANYDATA']._serialized_start=710
  _globals['_PINPUTANYDATA']._serialized_end=791
  _globals['_PVIEWRESPONSES']._serialized_start=793
  _globals['_PVIEWRESPONSES']._serialized_end=878
  _globals['_PINPUTARGUMENTS']._serialized_start=881
  _globals['_PINPUTARGUMENTS']._serialized_end=1298
  _globals['_PINPUTARGUMENTS_CONDITIONSENTRY']._serialized_start=243
  _globals['_PINPUTARGUMENTS_CONDITIONSENTRY']._serialized_end=310
  _globals['_PINPUTARGUMENTS_ATTRIBUTESENTRY']._serialized_start=1164
  _globals['_PINPUTARGUMENTS_ATTRIBUTESENTRY']._serialized_end=1231
  _globals['_PINPUTARGUMENTS_METASENTRY']._serialized_start=1233
  _globals['_PINPUTARGUMENTS_METASENTRY']._serialized_end=1298
  _globals['_PUPDATERESPONSES']._serialized_start=1301
  _globals['_PUPDATERESPONSES']._serialized_end=1493
  _globals['_PUPDATERESPONSES_AFFECTEDIDSENTRY']._serialized_start=1443
  _globals['_PUPDATERESPONSES_AFFECTEDIDSENTRY']._serialized_end=1493
  _globals['_PINSERTRESPONSES']._serialized_start=1496
  _globals['_PINSERTRESPONSES']._serialized_end=1765
  _globals['_PINSERTRESPONSES_IDSENTRY']._serialized_start=1652
  _globals['_PINSERTRESPONSES_IDSENTRY']._serialized_end=1694
  _globals['_PINSERTRESPONSES_METASENTRY']._serialized_start=1696
  _globals['_PINSERTRESPONSES_METASENTRY']._serialized_end=1765
# @@protoc_insertion_point(module_scope)
