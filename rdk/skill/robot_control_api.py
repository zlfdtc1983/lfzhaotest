#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
控制类定义了对机器人的所有操作，包括robot操作指令、rcu操作指令、机器人移动指令等。

通过调用Robot相关方法可以实现此功能

警告:
    充电过程中机器人不可运动。

    当电量不足时请及时充电。
"""

import grpc

from protopb.common import common_pb2
from protopb.robot_skill_api import robot_control_api_pb2, robot_control_api_pb2_grpc
from src.rdk.tools import tools


class RobotControlService(object):
    """
    机器人控制相关操作， 实现对机器人的各种操作
    """

    def __init__(self, grpc_url):
        """
        初始化方法

        :param grpc_url: gRPC服务器地址
        """
        print("RobotControlService init--")
        self.grpc_url = grpc_url
        print(grpc_url)
        channel = grpc.insecure_channel(grpc_url)
        self.stub = robot_control_api_pb2_grpc.RobotControlServiceStub(channel)

    def reboot_rcu(self, header):
        """
        重启RCU

        :param request: 设备相关信息.
                如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """

        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.RebootRcu(robot_request)
        return res_data

    def shutdown_rcu(self, header):
        """
        关闭RCU

        :param request: 设备相关信息.
                如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """

        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.ShutdownRcu(robot_request)
        return res_data

    def restart_app(self, header):
        """
        重启RCU上的Harix应用

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.RestartApp(robot_request)
        return res_data
        #return None

    def lock_rcu_screen(self, header):
        """
        锁屏

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.LockRcuScreen(robot_request)
        return res_data

    def light_rcu_screen(self, header):
        """
        点亮屏幕

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.LightRcuScreen(robot_request)
        return res_data

    def shutdown_robot(self, header):
        """
        关闭机器人

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.ShutdownRobot(robot_request)
        return res_data

    def wakeup_robot(self, header):
        """
        唤醒机器人

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.WakeupRobot(robot_request)
        return res_data

    def reset_robot(self, header):
        """
        重置机器人

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.ResetRobot(robot_request)
        return res_data

    def reboot_robot(self, header):
        """
        重启机器人

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.RebootRobot(robot_request)
        return res_data

    def reconnect_robot(self, header):
        """
        重连机器人

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.ReconnectRobot(robot_request)
        return res_data

    def get_robot_actions(self, header):
        """
        通知RCU上报动作列表与舞蹈列表

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.GetRobotActions(robot_request)
        return res_data

    def do_intent(self, header, request):
        """
        执行固定意图的任务

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        intent_request = robot_control_api_pb2.IntentRequest(
            common_req_info=tools.convert_header(header),
            intent_type=request["intent_type"],
            param=request["param"]
        )
        res_data = self.stub.DoIntent(intent_request)
        return res_data

    def do_action(self, header, input_request):
        """
        控制机器人执行某个动作
        :param input_request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        request = robot_control_api_pb2.ActionRequest(
            common_req_info=tools.convert_header(header),
            action=input_request["action"],
            param=input_request["params"]
        )

        res_data = self.stub.DoAction(request)
        print(res_data)
        return res_data

    def send_data(self, header, request):
        """
        发送数据到robot上
        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        send_data_request = robot_control_api_pb2.SendDataRequest(
            common_req_info=tools.convert_header(header),
            action=request["action"],
            param=request["params"]
        )

        res_data = self.stub.SendData(send_data_request)
        print(res_data)
        return res_data

    def move(self, header, data):
        """
        移动

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """

        print(data["map_model"])
        if data["map_model"] is not None:
            map_model = robot_control_api_pb2.MapModel(
                angle=data["map_model"]["angle"],
                speed=data["map_model"]["speed"],
                distance=data["map_model"]["distance"]

            )
            request = robot_control_api_pb2.MoveRequest(
                common_req_info=tools.convert_header(header),
                map_model=map_model
            )
            res_data = self.stub.Move(request)
            print(res_data)
            return res_data

        if data["v_model"] is not None:
            v_model = robot_control_api_pb2.VelocityModel(
                vx=data["v_model"]["vx"],
                vy=data["v_model"]["vy"],
                vw=data["v_model"]["vw"]
            )
            request = robot_control_api_pb2.MoveRequest(
                common_req_info=tools.convert_header(header),
                v_model=v_model
            )
            res_data = self.stub.Move(request)
            print(res_data)
            return res_data

        return None

    def stop(self, header):
        """
        停止

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )

        return self.stub.Stop(robot_request)

    def rotate(self, header, request):
        """
        旋转

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """

        rotate_request = robot_control_api_pb2.RotateRequest(
            common_req_info=tools.convert_header(header),
            module=request["module"],
            degree=request["degree"],
            speed=request["speed"]

        )

        res_data = self.stub.Rotate(rotate_request)
        print(res_data)
        return res_data

    def set_position(self, header, request):
        """
        设置机器人位置

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        robot_position = robot_control_api_pb2.RobotPosition(
            x=request["x"],
            y=request["y"],
            theta=request["theta"]

        )
        position_request = robot_control_api_pb2.PositionRequest(
            common_req_info=tools.convert_header(header),
            position=robot_position

        )

        res_data = self.stub.Rotate(position_request)
        print(res_data)
        return res_data

    def emergency_stop(self, header, request):
        """
        急停

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        position_request = robot_control_api_pb2.EmergencyStopRequest(
            common_req_info=tools.convert_header(header),
            emergency_stop_switch=request["emergency_stop_switch"]
        )

        res_data = self.stub.Rotate(position_request)
        print(res_data)
        return res_data
