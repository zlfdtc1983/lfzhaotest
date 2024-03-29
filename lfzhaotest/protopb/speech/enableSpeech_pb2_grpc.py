# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from protopb.speech import enableSpeech_pb2 as speech_dot_enableSpeech__pb2


class EnableSpeechStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.enable = channel.unary_unary(
        '/skill.asr.EnableSpeech/enable',
        request_serializer=speech_dot_enableSpeech__pb2.EnableRequest.SerializeToString,
        response_deserializer=speech_dot_enableSpeech__pb2.EnableResponse.FromString,
        )


class EnableSpeechServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def enable(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EnableSpeechServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'enable': grpc.unary_unary_rpc_method_handler(
          servicer.enable,
          request_deserializer=speech_dot_enableSpeech__pb2.EnableRequest.FromString,
          response_serializer=speech_dot_enableSpeech__pb2.EnableResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'skill.asr.EnableSpeech', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
