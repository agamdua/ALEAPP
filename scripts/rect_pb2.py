# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rect.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import scripts.privacy_pb2 as privacy__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rect.proto',
  package='android.graphics',
  syntax='proto2',
  serialized_options=_b('P\001'),
  serialized_pb=_b('\n\nrect.proto\x12\x10\x61ndroid.graphics\x1a\rprivacy.proto\"P\n\tRectProto\x12\x0c\n\x04left\x18\x01 \x01(\x05\x12\x0b\n\x03top\x18\x02 \x01(\x05\x12\r\n\x05right\x18\x03 \x01(\x05\x12\x0e\n\x06\x62ottom\x18\x04 \x01(\x05:\t\x9a\x9f\xd5\x87\x03\x03\x08\xc8\x01\x42\x02P\x01')
  ,
  dependencies=[privacy__pb2.DESCRIPTOR,])




_RECTPROTO = _descriptor.Descriptor(
  name='RectProto',
  full_name='android.graphics.RectProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='left', full_name='android.graphics.RectProto.left', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='top', full_name='android.graphics.RectProto.top', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right', full_name='android.graphics.RectProto.right', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bottom', full_name='android.graphics.RectProto.bottom', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\232\237\325\207\003\003\010\310\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=127,
)

DESCRIPTOR.message_types_by_name['RectProto'] = _RECTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RectProto = _reflection.GeneratedProtocolMessageType('RectProto', (_message.Message,), dict(
  DESCRIPTOR = _RECTPROTO,
  __module__ = 'rect_pb2'
  # @@protoc_insertion_point(class_scope:android.graphics.RectProto)
  ))
_sym_db.RegisterMessage(RectProto)


DESCRIPTOR._options = None
_RECTPROTO._options = None
# @@protoc_insertion_point(module_scope)
