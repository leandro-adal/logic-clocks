# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logic-clock.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11logic-clock.proto\"4\n\x07Request\x12\x14\n\x0clogical_time\x18\x01 \x01(\x05\x12\x13\n\x0bsender_port\x18\x02 \x01(\x05\"\n\n\x08Response2;\n\x0bLogicalTime\x12,\n\x13update_time_logical\x12\x08.Request\x1a\t.Response\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'logic_clock_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=21
  _REQUEST._serialized_end=73
  _RESPONSE._serialized_start=75
  _RESPONSE._serialized_end=85
  _LOGICALTIME._serialized_start=87
  _LOGICALTIME._serialized_end=146
# @@protoc_insertion_point(module_scope)
