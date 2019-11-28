# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: robot-mind/robot-mind.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import common_pb2 as common_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='robot-mind/robot-mind.proto',
  package='robotmind',
  syntax='proto3',
  serialized_options=_b('Z7cloudminds.com/harix/harix-skill-robot/proto/robot-mind'),
  serialized_pb=_b('\n\x1brobot-mind/robot-mind.proto\x12\trobotmind\x1a\x13\x63ommon/common.proto\"d\n\x12\x45nableSkillRequest\x12.\n\x0f\x63ommon_req_info\x18\x01 \x01(\x0b\x32\x15.common.CommonReqInfo\x12\x0f\n\x07\x61\x62ility\x18\x02 \x01(\x08\x12\r\n\x05param\x18\x03 \x01(\t\"V\n\x13\x45nableSkillResponse\x12/\n\x10\x63ommon_resp_info\x18\x01 \x01(\x0b\x32\x15.common.CommonRspInfo\x12\x0e\n\x06result\x18\x02 \x01(\t\"^\n\x11SkillEventRequest\x12.\n\x0f\x63ommon_req_info\x18\x01 \x01(\x0b\x32\x15.common.CommonReqInfo\x12\n\n\x02id\x18\x02 \x01(\t\x12\r\n\x05param\x18\x03 \x01(\t\"U\n\x12SkillEventResponse\x12/\n\x10\x63ommon_resp_info\x18\x01 \x01(\x0b\x32\x15.common.CommonRspInfo\x12\x0e\n\x06result\x18\x02 \x01(\t\"\\\n\x14RegisterSkillRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nskill_addr\x18\x02 \x01(\t\x12\x0e\n\x06skills\x18\x03 \x03(\t\x12\x12\n\nskill_info\x18\x04 \x01(\t\"Z\n\rActionRequest\x12.\n\x0f\x63ommon_req_info\x18\x01 \x01(\x0b\x32\x15.common.CommonReqInfo\x12\n\n\x02id\x18\x02 \x01(\t\x12\r\n\x05param\x18\x03 \x01(\t\"O\n\x0e\x41\x63tionResponse\x12/\n\x10\x63ommon_resp_info\x18\x01 \x01(\x0b\x32\x15.common.CommonRspInfo\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t2\xaa\x01\n\x11RobotSkillService\x12N\n\x0b\x45nableSkill\x12\x1d.robotmind.EnableSkillRequest\x1a\x1e.robotmind.EnableSkillResponse\"\x00\x12\x45\n\x0cHandleAction\x12\x18.robotmind.ActionRequest\x1a\x19.robotmind.ActionResponse\"\x00\x32\xf2\x01\n\x10RobotMindService\x12M\n\rRegisterSkill\x12\x1f.robotmind.RegisterSkillRequest\x1a\x19.robotmind.ActionResponse\"\x00\x12J\n\x11SendUnknownAction\x12\x18.robotmind.ActionRequest\x1a\x19.robotmind.ActionResponse\"\x00\x12\x43\n\nSendAction\x12\x18.robotmind.ActionRequest\x1a\x19.robotmind.ActionResponse\"\x00\x42\x39Z7cloudminds.com/harix/harix-skill-robot/proto/robot-mindb\x06proto3')
  ,
  dependencies=[common_dot_common__pb2.DESCRIPTOR,])




_ENABLESKILLREQUEST = _descriptor.Descriptor(
  name='EnableSkillRequest',
  full_name='robotmind.EnableSkillRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_req_info', full_name='robotmind.EnableSkillRequest.common_req_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ability', full_name='robotmind.EnableSkillRequest.ability', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='param', full_name='robotmind.EnableSkillRequest.param', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=63,
  serialized_end=163,
)


_ENABLESKILLRESPONSE = _descriptor.Descriptor(
  name='EnableSkillResponse',
  full_name='robotmind.EnableSkillResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_resp_info', full_name='robotmind.EnableSkillResponse.common_resp_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='robotmind.EnableSkillResponse.result', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=165,
  serialized_end=251,
)


_SKILLEVENTREQUEST = _descriptor.Descriptor(
  name='SkillEventRequest',
  full_name='robotmind.SkillEventRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_req_info', full_name='robotmind.SkillEventRequest.common_req_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='robotmind.SkillEventRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='param', full_name='robotmind.SkillEventRequest.param', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=253,
  serialized_end=347,
)


_SKILLEVENTRESPONSE = _descriptor.Descriptor(
  name='SkillEventResponse',
  full_name='robotmind.SkillEventResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_resp_info', full_name='robotmind.SkillEventResponse.common_resp_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='robotmind.SkillEventResponse.result', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=349,
  serialized_end=434,
)


_REGISTERSKILLREQUEST = _descriptor.Descriptor(
  name='RegisterSkillRequest',
  full_name='robotmind.RegisterSkillRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='robotmind.RegisterSkillRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skill_addr', full_name='robotmind.RegisterSkillRequest.skill_addr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skills', full_name='robotmind.RegisterSkillRequest.skills', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skill_info', full_name='robotmind.RegisterSkillRequest.skill_info', index=3,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=528,
)


_ACTIONREQUEST = _descriptor.Descriptor(
  name='ActionRequest',
  full_name='robotmind.ActionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_req_info', full_name='robotmind.ActionRequest.common_req_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='robotmind.ActionRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='param', full_name='robotmind.ActionRequest.param', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=530,
  serialized_end=620,
)


_ACTIONRESPONSE = _descriptor.Descriptor(
  name='ActionResponse',
  full_name='robotmind.ActionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_resp_info', full_name='robotmind.ActionResponse.common_resp_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='robotmind.ActionResponse.data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=622,
  serialized_end=701,
)

_ENABLESKILLREQUEST.fields_by_name['common_req_info'].message_type = common_dot_common__pb2._COMMONREQINFO
_ENABLESKILLRESPONSE.fields_by_name['common_resp_info'].message_type = common_dot_common__pb2._COMMONRSPINFO
_SKILLEVENTREQUEST.fields_by_name['common_req_info'].message_type = common_dot_common__pb2._COMMONREQINFO
_SKILLEVENTRESPONSE.fields_by_name['common_resp_info'].message_type = common_dot_common__pb2._COMMONRSPINFO
_ACTIONREQUEST.fields_by_name['common_req_info'].message_type = common_dot_common__pb2._COMMONREQINFO
_ACTIONRESPONSE.fields_by_name['common_resp_info'].message_type = common_dot_common__pb2._COMMONRSPINFO
DESCRIPTOR.message_types_by_name['EnableSkillRequest'] = _ENABLESKILLREQUEST
DESCRIPTOR.message_types_by_name['EnableSkillResponse'] = _ENABLESKILLRESPONSE
DESCRIPTOR.message_types_by_name['SkillEventRequest'] = _SKILLEVENTREQUEST
DESCRIPTOR.message_types_by_name['SkillEventResponse'] = _SKILLEVENTRESPONSE
DESCRIPTOR.message_types_by_name['RegisterSkillRequest'] = _REGISTERSKILLREQUEST
DESCRIPTOR.message_types_by_name['ActionRequest'] = _ACTIONREQUEST
DESCRIPTOR.message_types_by_name['ActionResponse'] = _ACTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EnableSkillRequest = _reflection.GeneratedProtocolMessageType('EnableSkillRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENABLESKILLREQUEST,
  '__module__' : 'robot_mind.robot_mind_pb2'
  # @@protoc_insertion_point(class_scope:robotmind.EnableSkillRequest)
  })
_sym_db.RegisterMessage(EnableSkillRequest)

EnableSkillResponse = _reflection.GeneratedProtocolMessageType('EnableSkillResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENABLESKILLRESPONSE,
  '__module__' : 'robot_mind.robot_mind_pb2'
  # @@protoc_insertion_point(class_scope:robotmind.EnableSkillResponse)
  })
_sym_db.RegisterMessage(EnableSkillResponse)

SkillEventRequest = _reflection.GeneratedProtocolMessageType('SkillEventRequest', (_message.Message,), {
  'DESCRIPTOR' : _SKILLEVENTREQUEST,
  '__module__' : 'robot_mind.robot_mind_pb2'
  # @@protoc_insertion_point(class_scope:robotmind.SkillEventRequest)
  })
_sym_db.RegisterMessage(SkillEventRequest)

SkillEventResponse = _reflection.GeneratedProtocolMessageType('SkillEventResponse', (_message.Message,), {
  'DESCRIPTOR' : _SKILLEVENTRESPONSE,
  '__module__' : 'robot_mind.robot_mind_pb2'
  # @@protoc_insertion_point(class_scope:robotmind.SkillEventResponse)
  })
_sym_db.RegisterMessage(SkillEventResponse)

RegisterSkillRequest = _reflection.GeneratedProtocolMessageType('RegisterSkillRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERSKILLREQUEST,
  '__module__' : 'robot_mind.robot_mind_pb2'
  # @@protoc_insertion_point(class_scope:robotmind.RegisterSkillRequest)
  })
_sym_db.RegisterMessage(RegisterSkillRequest)

ActionRequest = _reflection.GeneratedProtocolMessageType('ActionRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONREQUEST,
  '__module__' : 'robot_mind.robot_mind_pb2'
  # @@protoc_insertion_point(class_scope:robotmind.ActionRequest)
  })
_sym_db.RegisterMessage(ActionRequest)

ActionResponse = _reflection.GeneratedProtocolMessageType('ActionResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONRESPONSE,
  '__module__' : 'robot_mind.robot_mind_pb2'
  # @@protoc_insertion_point(class_scope:robotmind.ActionResponse)
  })
_sym_db.RegisterMessage(ActionResponse)


DESCRIPTOR._options = None

_ROBOTSKILLSERVICE = _descriptor.ServiceDescriptor(
  name='RobotSkillService',
  full_name='robotmind.RobotSkillService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=704,
  serialized_end=874,
  methods=[
  _descriptor.MethodDescriptor(
    name='EnableSkill',
    full_name='robotmind.RobotSkillService.EnableSkill',
    index=0,
    containing_service=None,
    input_type=_ENABLESKILLREQUEST,
    output_type=_ENABLESKILLRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='HandleAction',
    full_name='robotmind.RobotSkillService.HandleAction',
    index=1,
    containing_service=None,
    input_type=_ACTIONREQUEST,
    output_type=_ACTIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROBOTSKILLSERVICE)

DESCRIPTOR.services_by_name['RobotSkillService'] = _ROBOTSKILLSERVICE


_ROBOTMINDSERVICE = _descriptor.ServiceDescriptor(
  name='RobotMindService',
  full_name='robotmind.RobotMindService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=877,
  serialized_end=1119,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterSkill',
    full_name='robotmind.RobotMindService.RegisterSkill',
    index=0,
    containing_service=None,
    input_type=_REGISTERSKILLREQUEST,
    output_type=_ACTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendUnknownAction',
    full_name='robotmind.RobotMindService.SendUnknownAction',
    index=1,
    containing_service=None,
    input_type=_ACTIONREQUEST,
    output_type=_ACTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendAction',
    full_name='robotmind.RobotMindService.SendAction',
    index=2,
    containing_service=None,
    input_type=_ACTIONREQUEST,
    output_type=_ACTIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROBOTMINDSERVICE)

DESCRIPTOR.services_by_name['RobotMindService'] = _ROBOTMINDSERVICE

# @@protoc_insertion_point(module_scope)
