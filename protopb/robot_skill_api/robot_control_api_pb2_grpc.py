# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from protopb.robot_skill_api import robot_control_api_pb2 as robot__skill__api_dot_robot__control__api__pb2


class RobotControlServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RebootRcu = channel.unary_unary(
        '/robotSkillApi.RobotControlService/RebootRcu',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )
    self.ShutdownRcu = channel.unary_unary(
        '/robotSkillApi.RobotControlService/ShutdownRcu',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )
    self.RestartApp = channel.unary_unary(
        '/robotSkillApi.RobotControlService/RestartApp',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )
    self.LockRcuScreen = channel.unary_unary(
        '/robotSkillApi.RobotControlService/LockRcuScreen',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )
    self.LightRcuScreen = channel.unary_unary(
        '/robotSkillApi.RobotControlService/LightRcuScreen',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )
    self.ShutdownRobot = channel.unary_unary(
        '/robotSkillApi.RobotControlService/ShutdownRobot',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )
    self.WakeupRobot = channel.unary_unary(
        '/robotSkillApi.RobotControlService/WakeupRobot',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )
    self.ResetRobot = channel.unary_unary(
        '/robotSkillApi.RobotControlService/ResetRobot',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )
    self.RebootRobot = channel.unary_unary(
        '/robotSkillApi.RobotControlService/RebootRobot',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )
    self.ReconnectRobot = channel.unary_unary(
        '/robotSkillApi.RobotControlService/ReconnectRobot',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )
    self.GetRobotActions = channel.unary_unary(
        '/robotSkillApi.RobotControlService/GetRobotActions',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )
    self.DoIntent = channel.unary_unary(
        '/robotSkillApi.RobotControlService/DoIntent',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.IntentRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )
    self.DoAction = channel.unary_unary(
        '/robotSkillApi.RobotControlService/DoAction',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.ActionRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )
    self.SendData = channel.unary_unary(
        '/robotSkillApi.RobotControlService/SendData',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.SendDataRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )
    self.Move = channel.unary_unary(
        '/robotSkillApi.RobotControlService/Move',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.MoveRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )
    self.Stop = channel.unary_unary(
        '/robotSkillApi.RobotControlService/Stop',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )
    self.Rotate = channel.unary_unary(
        '/robotSkillApi.RobotControlService/Rotate',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.RotateRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )
    self.SetPosition = channel.unary_unary(
        '/robotSkillApi.RobotControlService/SetPosition',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.PositionRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )
    self.EmergencyStop = channel.unary_unary(
        '/robotSkillApi.RobotControlService/EmergencyStop',
        request_serializer=robot__skill__api_dot_robot__control__api__pb2.EmergencyStopRequest.SerializeToString,
        response_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.FromString,
        )


class RobotControlServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def RebootRcu(self, request, context):
    """重启RCU
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShutdownRcu(self, request, context):
    """关闭RCU
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RestartApp(self, request, context):
    """重启RCU APP
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def LockRcuScreen(self, request, context):
    """锁屏
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def LightRcuScreen(self, request, context):
    """点亮屏幕
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShutdownRobot(self, request, context):
    """关闭机器人
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WakeupRobot(self, request, context):
    """唤醒机器人
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ResetRobot(self, request, context):
    """重置机器人
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RebootRobot(self, request, context):
    """重启机器人
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReconnectRobot(self, request, context):
    """重连机器人
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRobotActions(self, request, context):
    """// 上传日志
    rpc EnableUploadLog (RobotRequest) returns (RobotResponse) {
    }
    通知RCU上报动作列表与舞蹈列表
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DoIntent(self, request, context):
    """执行固定意图的任务
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DoAction(self, request, context):
    """控制机器人执行某个动作
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendData(self, request, context):
    """向机器人发送业务数据
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Move(self, request, context):
    """移动
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Stop(self, request, context):
    """停止
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Rotate(self, request, context):
    """旋转
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetPosition(self, request, context):
    """设置机器人的位姿
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EmergencyStop(self, request, context):
    """急停
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RobotControlServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RebootRcu': grpc.unary_unary_rpc_method_handler(
          servicer.RebootRcu,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
      'ShutdownRcu': grpc.unary_unary_rpc_method_handler(
          servicer.ShutdownRcu,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
      'RestartApp': grpc.unary_unary_rpc_method_handler(
          servicer.RestartApp,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
      'LockRcuScreen': grpc.unary_unary_rpc_method_handler(
          servicer.LockRcuScreen,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
      'LightRcuScreen': grpc.unary_unary_rpc_method_handler(
          servicer.LightRcuScreen,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
      'ShutdownRobot': grpc.unary_unary_rpc_method_handler(
          servicer.ShutdownRobot,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
      'WakeupRobot': grpc.unary_unary_rpc_method_handler(
          servicer.WakeupRobot,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
      'ResetRobot': grpc.unary_unary_rpc_method_handler(
          servicer.ResetRobot,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
      'RebootRobot': grpc.unary_unary_rpc_method_handler(
          servicer.RebootRobot,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
      'ReconnectRobot': grpc.unary_unary_rpc_method_handler(
          servicer.ReconnectRobot,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
      'GetRobotActions': grpc.unary_unary_rpc_method_handler(
          servicer.GetRobotActions,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
      'DoIntent': grpc.unary_unary_rpc_method_handler(
          servicer.DoIntent,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.IntentRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
      'DoAction': grpc.unary_unary_rpc_method_handler(
          servicer.DoAction,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.ActionRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
      'SendData': grpc.unary_unary_rpc_method_handler(
          servicer.SendData,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.SendDataRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
      'Move': grpc.unary_unary_rpc_method_handler(
          servicer.Move,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.MoveRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
      'Stop': grpc.unary_unary_rpc_method_handler(
          servicer.Stop,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.RobotRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
      'Rotate': grpc.unary_unary_rpc_method_handler(
          servicer.Rotate,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.RotateRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
      'SetPosition': grpc.unary_unary_rpc_method_handler(
          servicer.SetPosition,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.PositionRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
      'EmergencyStop': grpc.unary_unary_rpc_method_handler(
          servicer.EmergencyStop,
          request_deserializer=robot__skill__api_dot_robot__control__api__pb2.EmergencyStopRequest.FromString,
          response_serializer=robot__skill__api_dot_robot__control__api__pb2.RobotResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'robotSkillApi.RobotControlService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
