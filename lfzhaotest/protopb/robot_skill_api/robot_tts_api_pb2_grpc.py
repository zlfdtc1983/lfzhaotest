# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from protopb.common import qa_pb2 as common_dot_qa__pb2
from protopb.robot_skill_api import robot_tts_api_pb2 as robot__skill__api_dot_robot__tts__api__pb2


class RobotTtsServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Speak = channel.unary_unary(
        '/robotSkillApi.RobotTtsService/Speak',
        request_serializer=robot__skill__api_dot_robot__tts__api__pb2.SpeakRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__tts__api__pb2.SpeakResponse.FromString,
        )
    self.SendQa = channel.unary_unary(
        '/robotSkillApi.RobotTtsService/SendQa',
        request_serializer=common_dot_qa__pb2.SwMessage.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__tts__api__pb2.SpeakResponse.FromString,
        )


class RobotTtsServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Speak(self, request, context):
    """语音播报
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendQa(self, request, context):
    """发送QA，包括问题和答案
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RobotTtsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Speak': grpc.unary_unary_rpc_method_handler(
          servicer.Speak,
          request_deserializer=robot__skill__api_dot_robot__tts__api__pb2.SpeakRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__tts__api__pb2.SpeakResponse.SerializeToString,
      ),
      'SendQa': grpc.unary_unary_rpc_method_handler(
          servicer.SendQa,
          request_deserializer=common_dot_qa__pb2.SwMessage.FromString,
          response_serializer=robot__skill__api_dot_robot__tts__api__pb2.SpeakResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'robotSkillApi.RobotTtsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
