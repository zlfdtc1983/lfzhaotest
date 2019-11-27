#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
语言模块，本模块封装了机器人运动语音相关的类、方法、结构
"""

import grpc
from protopb.common import common_pb2
from protopb.robot_skill_api import robot_tts_api_pb2, robot_tts_api_pb2_grpc
from src.rdk.tools import tools

class RobotTtsService(object):
    """
    语音相关类
    """

    def __init__(self, grpc_url):
        """
        初始化方法

        :param grpc_url: gRPC服务器地址
        """
        print("RobotTtsService init--")
        self.grpc_url = grpc_url
        print(grpc_url)
        channel = grpc.insecure_channel(grpc_url)
        self.stub = robot_tts_api_pb2_grpc.RobotTtsServiceStub(channel)


    def Speak(self, header, data):
        """
        说一段话

        :param request: 语音相关信息
        :return:
        """

        tts = robot_tts_api_pb2.Tts(text=data["text"], lang=data["lang"])
        request = robot_tts_api_pb2.SpeakRequest(
            common_req_info=tools.convert_header(header),
            tts=[tts]
        )

        res_data = self.stub.Speak(request)
        print(res_data)
        return res_data
