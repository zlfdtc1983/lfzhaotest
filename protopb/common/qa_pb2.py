# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/qa.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from protopb.common import common_pb2 as common_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/qa.proto',
  package='common',
  syntax='proto3',
  serialized_options=_b('\n\033com.cloudminds.harix.commonZ3cloudminds.com/harix/harix-skill-robot/proto/common'),
  serialized_pb=_b('\n\x0f\x63ommon/qa.proto\x12\x06\x63ommon\x1a\x1cgoogle/protobuf/struct.proto\x1a\x13\x63ommon/common.proto\"\x86\n\n\tSwMessage\x12.\n\x0f\x63ommon_req_info\x18\x01 \x01(\x0b\x32\x15.common.CommonReqInfo\x12(\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1a.common.SwMessage.SwQaData\x1a\x9e\t\n\x08SwQaData\x12\x35\n\x08question\x18\x01 \x01(\x0b\x32#.common.SwMessage.SwQaData.Question\x12\x31\n\x06\x61nswer\x18\x02 \x03(\x0b\x32!.common.SwMessage.SwQaData.Answer\x12\x33\n\x04tree\x18\x03 \x01(\x0b\x32%.common.SwMessage.SwQaData.DialogTree\x12\x10\n\x08similars\x18\x04 \x03(\t\x12\x35\n\x07\x63ontext\x18\x05 \x01(\x0b\x32$.common.SwMessage.SwQaData.HaContext\x1ah\n\x08Question\x12\x0c\n\x04lang\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x0e\n\x06qaFlag\x18\x03 \x01(\t\x12\x12\n\nquestionId\x18\x04 \x01(\t\x12\r\n\x05\x61udio\x18\x05 \x01(\t\x12\r\n\x05image\x18\x06 \x01(\t\x1a\xcc\x03\n\x06\x41nswer\x12\r\n\x05score\x18\x01 \x01(\x02\x12\x11\n\tresponder\x18\x02 \x01(\t\x12\x32\n\x03tts\x18\x03 \x03(\x0b\x32%.common.SwMessage.SwQaData.Answer.Tts\x12\r\n\x05image\x18\x04 \x03(\t\x12\x0e\n\x06qrCode\x18\x05 \x01(\t\x1a\xcc\x02\n\x03Tts\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0c\n\x04lang\x18\x02 \x01(\t\x12?\n\x06\x61\x63tion\x18\x03 \x01(\x0b\x32/.common.SwMessage.SwQaData.Answer.Tts.TtsAction\x12\r\n\x05\x61udio\x18\x04 \x01(\t\x12\r\n\x05\x65moji\x18\x05 \x01(\t\x12\x0f\n\x07payload\x18\x06 \x01(\t\x12\x0c\n\x04type\x18\x07 \x01(\t\x1a\xaa\x01\n\tTtsAction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12I\n\x05param\x18\x02 \x03(\x0b\x32:.common.SwMessage.SwQaData.Answer.Tts.TtsAction.ParamEntry\x1a\x44\n\nParamEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value:\x02\x38\x01\x1a\x9e\x01\n\nDialogTree\x12\x14\n\x0c\x63urrentstate\x18\x01 \x01(\t\x12\x46\n\x07subtree\x18\x02 \x03(\x0b\x32\x35.common.SwMessage.SwQaData.DialogTree.DialogTreeState\x1a\x32\n\x0f\x44ialogTreeState\x12\r\n\x05state\x18\x01 \x01(\t\x12\x10\n\x08template\x18\x02 \x01(\t\x1a\xcf\x01\n\tHaContext\x12\x45\n\x07history\x18\x01 \x03(\x0b\x32\x34.common.SwMessage.SwQaData.HaContext.HaQaHistoryItem\x1a{\n\x0fHaQaHistoryItem\x12\x35\n\x08question\x18\x01 \x01(\x0b\x32#.common.SwMessage.SwQaData.Question\x12\x31\n\x06\x61nswer\x18\x02 \x03(\x0b\x32!.common.SwMessage.SwQaData.AnswerBR\n\x1b\x63om.cloudminds.harix.commonZ3cloudminds.com/harix/harix-skill-robot/proto/commonb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,common_dot_common__pb2.DESCRIPTOR,])




_SWMESSAGE_SWQADATA_QUESTION = _descriptor.Descriptor(
  name='Question',
  full_name='common.SwMessage.SwQaData.Question',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lang', full_name='common.SwMessage.SwQaData.Question.lang', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='common.SwMessage.SwQaData.Question.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qaFlag', full_name='common.SwMessage.SwQaData.Question.qaFlag', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='questionId', full_name='common.SwMessage.SwQaData.Question.questionId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audio', full_name='common.SwMessage.SwQaData.Question.audio', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='common.SwMessage.SwQaData.Question.image', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=427,
  serialized_end=531,
)

_SWMESSAGE_SWQADATA_ANSWER_TTS_TTSACTION_PARAMENTRY = _descriptor.Descriptor(
  name='ParamEntry',
  full_name='common.SwMessage.SwQaData.Answer.Tts.TtsAction.ParamEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='common.SwMessage.SwQaData.Answer.Tts.TtsAction.ParamEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='common.SwMessage.SwQaData.Answer.Tts.TtsAction.ParamEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=926,
  serialized_end=994,
)

_SWMESSAGE_SWQADATA_ANSWER_TTS_TTSACTION = _descriptor.Descriptor(
  name='TtsAction',
  full_name='common.SwMessage.SwQaData.Answer.Tts.TtsAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='common.SwMessage.SwQaData.Answer.Tts.TtsAction.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='param', full_name='common.SwMessage.SwQaData.Answer.Tts.TtsAction.param', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SWMESSAGE_SWQADATA_ANSWER_TTS_TTSACTION_PARAMENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=824,
  serialized_end=994,
)

_SWMESSAGE_SWQADATA_ANSWER_TTS = _descriptor.Descriptor(
  name='Tts',
  full_name='common.SwMessage.SwQaData.Answer.Tts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='common.SwMessage.SwQaData.Answer.Tts.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lang', full_name='common.SwMessage.SwQaData.Answer.Tts.lang', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='common.SwMessage.SwQaData.Answer.Tts.action', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audio', full_name='common.SwMessage.SwQaData.Answer.Tts.audio', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='emoji', full_name='common.SwMessage.SwQaData.Answer.Tts.emoji', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='common.SwMessage.SwQaData.Answer.Tts.payload', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='common.SwMessage.SwQaData.Answer.Tts.type', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SWMESSAGE_SWQADATA_ANSWER_TTS_TTSACTION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=662,
  serialized_end=994,
)

_SWMESSAGE_SWQADATA_ANSWER = _descriptor.Descriptor(
  name='Answer',
  full_name='common.SwMessage.SwQaData.Answer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='score', full_name='common.SwMessage.SwQaData.Answer.score', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='responder', full_name='common.SwMessage.SwQaData.Answer.responder', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tts', full_name='common.SwMessage.SwQaData.Answer.tts', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='common.SwMessage.SwQaData.Answer.image', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qrCode', full_name='common.SwMessage.SwQaData.Answer.qrCode', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SWMESSAGE_SWQADATA_ANSWER_TTS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=534,
  serialized_end=994,
)

_SWMESSAGE_SWQADATA_DIALOGTREE_DIALOGTREESTATE = _descriptor.Descriptor(
  name='DialogTreeState',
  full_name='common.SwMessage.SwQaData.DialogTree.DialogTreeState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='common.SwMessage.SwQaData.DialogTree.DialogTreeState.state', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='template', full_name='common.SwMessage.SwQaData.DialogTree.DialogTreeState.template', index=1,
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
  serialized_start=1105,
  serialized_end=1155,
)

_SWMESSAGE_SWQADATA_DIALOGTREE = _descriptor.Descriptor(
  name='DialogTree',
  full_name='common.SwMessage.SwQaData.DialogTree',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currentstate', full_name='common.SwMessage.SwQaData.DialogTree.currentstate', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subtree', full_name='common.SwMessage.SwQaData.DialogTree.subtree', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SWMESSAGE_SWQADATA_DIALOGTREE_DIALOGTREESTATE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=997,
  serialized_end=1155,
)

_SWMESSAGE_SWQADATA_HACONTEXT_HAQAHISTORYITEM = _descriptor.Descriptor(
  name='HaQaHistoryItem',
  full_name='common.SwMessage.SwQaData.HaContext.HaQaHistoryItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='question', full_name='common.SwMessage.SwQaData.HaContext.HaQaHistoryItem.question', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='answer', full_name='common.SwMessage.SwQaData.HaContext.HaQaHistoryItem.answer', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1242,
  serialized_end=1365,
)

_SWMESSAGE_SWQADATA_HACONTEXT = _descriptor.Descriptor(
  name='HaContext',
  full_name='common.SwMessage.SwQaData.HaContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='history', full_name='common.SwMessage.SwQaData.HaContext.history', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SWMESSAGE_SWQADATA_HACONTEXT_HAQAHISTORYITEM, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1158,
  serialized_end=1365,
)

_SWMESSAGE_SWQADATA = _descriptor.Descriptor(
  name='SwQaData',
  full_name='common.SwMessage.SwQaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='question', full_name='common.SwMessage.SwQaData.question', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='answer', full_name='common.SwMessage.SwQaData.answer', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tree', full_name='common.SwMessage.SwQaData.tree', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='similars', full_name='common.SwMessage.SwQaData.similars', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='context', full_name='common.SwMessage.SwQaData.context', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SWMESSAGE_SWQADATA_QUESTION, _SWMESSAGE_SWQADATA_ANSWER, _SWMESSAGE_SWQADATA_DIALOGTREE, _SWMESSAGE_SWQADATA_HACONTEXT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=183,
  serialized_end=1365,
)

_SWMESSAGE = _descriptor.Descriptor(
  name='SwMessage',
  full_name='common.SwMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_req_info', full_name='common.SwMessage.common_req_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='common.SwMessage.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SWMESSAGE_SWQADATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=1365,
)

_SWMESSAGE_SWQADATA_QUESTION.containing_type = _SWMESSAGE_SWQADATA
_SWMESSAGE_SWQADATA_ANSWER_TTS_TTSACTION_PARAMENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_SWMESSAGE_SWQADATA_ANSWER_TTS_TTSACTION_PARAMENTRY.containing_type = _SWMESSAGE_SWQADATA_ANSWER_TTS_TTSACTION
_SWMESSAGE_SWQADATA_ANSWER_TTS_TTSACTION.fields_by_name['param'].message_type = _SWMESSAGE_SWQADATA_ANSWER_TTS_TTSACTION_PARAMENTRY
_SWMESSAGE_SWQADATA_ANSWER_TTS_TTSACTION.containing_type = _SWMESSAGE_SWQADATA_ANSWER_TTS
_SWMESSAGE_SWQADATA_ANSWER_TTS.fields_by_name['action'].message_type = _SWMESSAGE_SWQADATA_ANSWER_TTS_TTSACTION
_SWMESSAGE_SWQADATA_ANSWER_TTS.containing_type = _SWMESSAGE_SWQADATA_ANSWER
_SWMESSAGE_SWQADATA_ANSWER.fields_by_name['tts'].message_type = _SWMESSAGE_SWQADATA_ANSWER_TTS
_SWMESSAGE_SWQADATA_ANSWER.containing_type = _SWMESSAGE_SWQADATA
_SWMESSAGE_SWQADATA_DIALOGTREE_DIALOGTREESTATE.containing_type = _SWMESSAGE_SWQADATA_DIALOGTREE
_SWMESSAGE_SWQADATA_DIALOGTREE.fields_by_name['subtree'].message_type = _SWMESSAGE_SWQADATA_DIALOGTREE_DIALOGTREESTATE
_SWMESSAGE_SWQADATA_DIALOGTREE.containing_type = _SWMESSAGE_SWQADATA
_SWMESSAGE_SWQADATA_HACONTEXT_HAQAHISTORYITEM.fields_by_name['question'].message_type = _SWMESSAGE_SWQADATA_QUESTION
_SWMESSAGE_SWQADATA_HACONTEXT_HAQAHISTORYITEM.fields_by_name['answer'].message_type = _SWMESSAGE_SWQADATA_ANSWER
_SWMESSAGE_SWQADATA_HACONTEXT_HAQAHISTORYITEM.containing_type = _SWMESSAGE_SWQADATA_HACONTEXT
_SWMESSAGE_SWQADATA_HACONTEXT.fields_by_name['history'].message_type = _SWMESSAGE_SWQADATA_HACONTEXT_HAQAHISTORYITEM
_SWMESSAGE_SWQADATA_HACONTEXT.containing_type = _SWMESSAGE_SWQADATA
_SWMESSAGE_SWQADATA.fields_by_name['question'].message_type = _SWMESSAGE_SWQADATA_QUESTION
_SWMESSAGE_SWQADATA.fields_by_name['answer'].message_type = _SWMESSAGE_SWQADATA_ANSWER
_SWMESSAGE_SWQADATA.fields_by_name['tree'].message_type = _SWMESSAGE_SWQADATA_DIALOGTREE
_SWMESSAGE_SWQADATA.fields_by_name['context'].message_type = _SWMESSAGE_SWQADATA_HACONTEXT
_SWMESSAGE_SWQADATA.containing_type = _SWMESSAGE
_SWMESSAGE.fields_by_name['common_req_info'].message_type = common_dot_common__pb2._COMMONREQINFO
_SWMESSAGE.fields_by_name['data'].message_type = _SWMESSAGE_SWQADATA
DESCRIPTOR.message_types_by_name['SwMessage'] = _SWMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SwMessage = _reflection.GeneratedProtocolMessageType('SwMessage', (_message.Message,), {

  'SwQaData' : _reflection.GeneratedProtocolMessageType('SwQaData', (_message.Message,), {

    'Question' : _reflection.GeneratedProtocolMessageType('Question', (_message.Message,), {
      'DESCRIPTOR' : _SWMESSAGE_SWQADATA_QUESTION,
      '__module__' : 'common.qa_pb2'
      # @@protoc_insertion_point(class_scope:common.SwMessage.SwQaData.Question)
      })
    ,

    'Answer' : _reflection.GeneratedProtocolMessageType('Answer', (_message.Message,), {

      'Tts' : _reflection.GeneratedProtocolMessageType('Tts', (_message.Message,), {

        'TtsAction' : _reflection.GeneratedProtocolMessageType('TtsAction', (_message.Message,), {

          'ParamEntry' : _reflection.GeneratedProtocolMessageType('ParamEntry', (_message.Message,), {
            'DESCRIPTOR' : _SWMESSAGE_SWQADATA_ANSWER_TTS_TTSACTION_PARAMENTRY,
            '__module__' : 'common.qa_pb2'
            # @@protoc_insertion_point(class_scope:common.SwMessage.SwQaData.Answer.Tts.TtsAction.ParamEntry)
            })
          ,
          'DESCRIPTOR' : _SWMESSAGE_SWQADATA_ANSWER_TTS_TTSACTION,
          '__module__' : 'common.qa_pb2'
          # @@protoc_insertion_point(class_scope:common.SwMessage.SwQaData.Answer.Tts.TtsAction)
          })
        ,
        'DESCRIPTOR' : _SWMESSAGE_SWQADATA_ANSWER_TTS,
        '__module__' : 'common.qa_pb2'
        # @@protoc_insertion_point(class_scope:common.SwMessage.SwQaData.Answer.Tts)
        })
      ,
      'DESCRIPTOR' : _SWMESSAGE_SWQADATA_ANSWER,
      '__module__' : 'common.qa_pb2'
      # @@protoc_insertion_point(class_scope:common.SwMessage.SwQaData.Answer)
      })
    ,

    'DialogTree' : _reflection.GeneratedProtocolMessageType('DialogTree', (_message.Message,), {

      'DialogTreeState' : _reflection.GeneratedProtocolMessageType('DialogTreeState', (_message.Message,), {
        'DESCRIPTOR' : _SWMESSAGE_SWQADATA_DIALOGTREE_DIALOGTREESTATE,
        '__module__' : 'common.qa_pb2'
        # @@protoc_insertion_point(class_scope:common.SwMessage.SwQaData.DialogTree.DialogTreeState)
        })
      ,
      'DESCRIPTOR' : _SWMESSAGE_SWQADATA_DIALOGTREE,
      '__module__' : 'common.qa_pb2'
      # @@protoc_insertion_point(class_scope:common.SwMessage.SwQaData.DialogTree)
      })
    ,

    'HaContext' : _reflection.GeneratedProtocolMessageType('HaContext', (_message.Message,), {

      'HaQaHistoryItem' : _reflection.GeneratedProtocolMessageType('HaQaHistoryItem', (_message.Message,), {
        'DESCRIPTOR' : _SWMESSAGE_SWQADATA_HACONTEXT_HAQAHISTORYITEM,
        '__module__' : 'common.qa_pb2'
        # @@protoc_insertion_point(class_scope:common.SwMessage.SwQaData.HaContext.HaQaHistoryItem)
        })
      ,
      'DESCRIPTOR' : _SWMESSAGE_SWQADATA_HACONTEXT,
      '__module__' : 'common.qa_pb2'
      # @@protoc_insertion_point(class_scope:common.SwMessage.SwQaData.HaContext)
      })
    ,
    'DESCRIPTOR' : _SWMESSAGE_SWQADATA,
    '__module__' : 'common.qa_pb2'
    # @@protoc_insertion_point(class_scope:common.SwMessage.SwQaData)
    })
  ,
  'DESCRIPTOR' : _SWMESSAGE,
  '__module__' : 'common.qa_pb2'
  # @@protoc_insertion_point(class_scope:common.SwMessage)
  })
_sym_db.RegisterMessage(SwMessage)
_sym_db.RegisterMessage(SwMessage.SwQaData)
_sym_db.RegisterMessage(SwMessage.SwQaData.Question)
_sym_db.RegisterMessage(SwMessage.SwQaData.Answer)
_sym_db.RegisterMessage(SwMessage.SwQaData.Answer.Tts)
_sym_db.RegisterMessage(SwMessage.SwQaData.Answer.Tts.TtsAction)
_sym_db.RegisterMessage(SwMessage.SwQaData.Answer.Tts.TtsAction.ParamEntry)
_sym_db.RegisterMessage(SwMessage.SwQaData.DialogTree)
_sym_db.RegisterMessage(SwMessage.SwQaData.DialogTree.DialogTreeState)
_sym_db.RegisterMessage(SwMessage.SwQaData.HaContext)
_sym_db.RegisterMessage(SwMessage.SwQaData.HaContext.HaQaHistoryItem)


DESCRIPTOR._options = None
_SWMESSAGE_SWQADATA_ANSWER_TTS_TTSACTION_PARAMENTRY._options = None
# @@protoc_insertion_point(module_scope)
