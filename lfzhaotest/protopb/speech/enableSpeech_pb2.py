# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: speech/enableSpeech.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protopb.common import common_pb2 as common_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='speech/enableSpeech.proto',
  package='skill.asr',
  syntax='proto3',
  serialized_options=_b('\n\036com.cloudminds.harix.skill.asrB\021EnableSpeechProtoP\001'),
  serialized_pb=_b('\n\x19speech/enableSpeech.proto\x12\tskill.asr\x1a\x13\x63ommon/common.proto\"\xbb\x01\n\rEnableRequest\x12.\n\x0f\x63ommon_req_info\x18\x01 \x01(\x0b\x32\x15.common.CommonReqInfo\x12\x32\n\x08sub_type\x18\x02 \x01(\x0e\x32 .skill.asr.EnableRequest.SubType\x12\x0e\n\x06\x65nable\x18\x03 \x01(\x08\x12\x10\n\x08sub_addr\x18\x04 \x01(\t\"$\n\x07SubType\x12\r\n\tRECEPTION\x10\x00\x12\n\n\x06\x44IALOG\x10\x01\"P\n\x0e\x45nableResponse\x12.\n\x0f\x63ommon_rsp_info\x18\x01 \x01(\x0b\x32\x15.common.CommonRspInfo\x12\x0e\n\x06\x65nable\x18\x02 \x01(\x08\x32O\n\x0c\x45nableSpeech\x12?\n\x06\x65nable\x12\x18.skill.asr.EnableRequest\x1a\x19.skill.asr.EnableResponse\"\x00\x42\x35\n\x1e\x63om.cloudminds.harix.skill.asrB\x11\x45nableSpeechProtoP\x01\x62\x06proto3')
  ,
  dependencies=[common_dot_common__pb2.DESCRIPTOR,])



_ENABLEREQUEST_SUBTYPE = _descriptor.EnumDescriptor(
  name='SubType',
  full_name='skill.asr.EnableRequest.SubType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RECEPTION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIALOG', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=213,
  serialized_end=249,
)
_sym_db.RegisterEnumDescriptor(_ENABLEREQUEST_SUBTYPE)


_ENABLEREQUEST = _descriptor.Descriptor(
  name='EnableRequest',
  full_name='skill.asr.EnableRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_req_info', full_name='skill.asr.EnableRequest.common_req_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sub_type', full_name='skill.asr.EnableRequest.sub_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable', full_name='skill.asr.EnableRequest.enable', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sub_addr', full_name='skill.asr.EnableRequest.sub_addr', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENABLEREQUEST_SUBTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=249,
)


_ENABLERESPONSE = _descriptor.Descriptor(
  name='EnableResponse',
  full_name='skill.asr.EnableResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_rsp_info', full_name='skill.asr.EnableResponse.common_rsp_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable', full_name='skill.asr.EnableResponse.enable', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=251,
  serialized_end=331,
)

_ENABLEREQUEST.fields_by_name['common_req_info'].message_type = common_dot_common__pb2._COMMONREQINFO
_ENABLEREQUEST.fields_by_name['sub_type'].enum_type = _ENABLEREQUEST_SUBTYPE
_ENABLEREQUEST_SUBTYPE.containing_type = _ENABLEREQUEST
_ENABLERESPONSE.fields_by_name['common_rsp_info'].message_type = common_dot_common__pb2._COMMONRSPINFO
DESCRIPTOR.message_types_by_name['EnableRequest'] = _ENABLEREQUEST
DESCRIPTOR.message_types_by_name['EnableResponse'] = _ENABLERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EnableRequest = _reflection.GeneratedProtocolMessageType('EnableRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENABLEREQUEST,
  '__module__' : 'speech.enableSpeech_pb2'
  # @@protoc_insertion_point(class_scope:skill.asr.EnableRequest)
  })
_sym_db.RegisterMessage(EnableRequest)

EnableResponse = _reflection.GeneratedProtocolMessageType('EnableResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENABLERESPONSE,
  '__module__' : 'speech.enableSpeech_pb2'
  # @@protoc_insertion_point(class_scope:skill.asr.EnableResponse)
  })
_sym_db.RegisterMessage(EnableResponse)


DESCRIPTOR._options = None

_ENABLESPEECH = _descriptor.ServiceDescriptor(
  name='EnableSpeech',
  full_name='skill.asr.EnableSpeech',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=333,
  serialized_end=412,
  methods=[
  _descriptor.MethodDescriptor(
    name='enable',
    full_name='skill.asr.EnableSpeech.enable',
    index=0,
    containing_service=None,
    input_type=_ENABLEREQUEST,
    output_type=_ENABLERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENABLESPEECH)

DESCRIPTOR.services_by_name['EnableSpeech'] = _ENABLESPEECH

# @@protoc_insertion_point(module_scope)
