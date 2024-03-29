# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from protopb.robot_skill_api import robot_config_api_pb2 as robot__skill__api_dot_robot__config__api__pb2


class RobotConfigServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ConfigRobot = channel.unary_unary(
        '/robotSkillApi.RobotConfigService/ConfigRobot',
        request_serializer=robot__skill__api_dot_robot__config__api__pb2.ConfigRobotRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__config__api__pb2.RobotConfigResponse.FromString,
        )
    self.GetRobotState = channel.unary_unary(
        '/robotSkillApi.RobotConfigService/GetRobotState',
        request_serializer=robot__skill__api_dot_robot__config__api__pb2.GetRobotStateRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__config__api__pb2.RobotConfigResponse.FromString,
        )
    self.ConfigRecordMedia = channel.unary_unary(
        '/robotSkillApi.RobotConfigService/ConfigRecordMedia',
        request_serializer=robot__skill__api_dot_robot__config__api__pb2.ConfigRecordMediaRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__config__api__pb2.RobotConfigResponse.FromString,
        )
    self.ConfigAsr = channel.unary_unary(
        '/robotSkillApi.RobotConfigService/ConfigAsr',
        request_serializer=robot__skill__api_dot_robot__config__api__pb2.ConfigAsrRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__config__api__pb2.RobotConfigResponse.FromString,
        )
    self.ConfigFr = channel.unary_unary(
        '/robotSkillApi.RobotConfigService/ConfigFr',
        request_serializer=robot__skill__api_dot_robot__config__api__pb2.ConfigFrRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__config__api__pb2.RobotConfigResponse.FromString,
        )
    self.ConfigFaceCam = channel.unary_unary(
        '/robotSkillApi.RobotConfigService/ConfigFaceCam',
        request_serializer=robot__skill__api_dot_robot__config__api__pb2.ConfigFaceCamRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__config__api__pb2.RobotConfigResponse.FromString,
        )
    self.ConfigScreenShot = channel.unary_unary(
        '/robotSkillApi.RobotConfigService/ConfigScreenShot',
        request_serializer=robot__skill__api_dot_robot__config__api__pb2.ConfigScreenShotRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__config__api__pb2.RobotConfigResponse.FromString,
        )


class RobotConfigServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ConfigRobot(self, request, context):
    """配置机器人参数
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRobotState(self, request, context):
    """查询机器人参数
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ConfigRecordMedia(self, request, context):
    """视频录制设置
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ConfigAsr(self, request, context):
    """控制ARS开/关
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ConfigFr(self, request, context):
    """控制识别功能开/关
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ConfigFaceCam(self, request, context):
    """控制识别功能开/关
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ConfigScreenShot(self, request, context):
    """控制短视频与截图录制
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RobotConfigServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ConfigRobot': grpc.unary_unary_rpc_method_handler(
          servicer.ConfigRobot,
          request_deserializer=robot__skill__api_dot_robot__config__api__pb2.ConfigRobotRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__config__api__pb2.RobotConfigResponse.SerializeToString,
      ),
      'GetRobotState': grpc.unary_unary_rpc_method_handler(
          servicer.GetRobotState,
          request_deserializer=robot__skill__api_dot_robot__config__api__pb2.GetRobotStateRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__config__api__pb2.RobotConfigResponse.SerializeToString,
      ),
      'ConfigRecordMedia': grpc.unary_unary_rpc_method_handler(
          servicer.ConfigRecordMedia,
          request_deserializer=robot__skill__api_dot_robot__config__api__pb2.ConfigRecordMediaRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__config__api__pb2.RobotConfigResponse.SerializeToString,
      ),
      'ConfigAsr': grpc.unary_unary_rpc_method_handler(
          servicer.ConfigAsr,
          request_deserializer=robot__skill__api_dot_robot__config__api__pb2.ConfigAsrRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__config__api__pb2.RobotConfigResponse.SerializeToString,
      ),
      'ConfigFr': grpc.unary_unary_rpc_method_handler(
          servicer.ConfigFr,
          request_deserializer=robot__skill__api_dot_robot__config__api__pb2.ConfigFrRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__config__api__pb2.RobotConfigResponse.SerializeToString,
      ),
      'ConfigFaceCam': grpc.unary_unary_rpc_method_handler(
          servicer.ConfigFaceCam,
          request_deserializer=robot__skill__api_dot_robot__config__api__pb2.ConfigFaceCamRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__config__api__pb2.RobotConfigResponse.SerializeToString,
      ),
      'ConfigScreenShot': grpc.unary_unary_rpc_method_handler(
          servicer.ConfigScreenShot,
          request_deserializer=robot__skill__api_dot_robot__config__api__pb2.ConfigScreenShotRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__config__api__pb2.RobotConfigResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'robotSkillApi.RobotConfigService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
