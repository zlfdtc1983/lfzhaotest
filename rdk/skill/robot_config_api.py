#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
配置类模块，本模块封装了对机器人进行配置的类、方法、结构
"""

import grpc
from protopb.common import common_pb2
from protopb.robot_skill_api import robot_config_api_pb2, robot_config_api_pb2_grpc
from src.rdk.tools import tools


class RobotConfigService(object):

    def __init__(self, grpc_url):
        """
        初始化方法

        :param grpc_url: gRPC服务器地址
        """
        print("RobotConfigService init--")
        self.grpc_url = grpc_url
        channel = grpc.insecure_channel(grpc_url)
        self.stub = robot_config_api_pb2_grpc.RobotConfigServiceStub(channel)

    def config_robot(self, header, request):
        """
        配置机器人参数

        :param request: 配置信息
        :param header: robot基本信息
        :return:
        """
        configRobotRequest = robot_config_api_pb2.ConfigRobotRequest(
            common_req_info=tools.convert_header(header),
            config_names=request["config_names"],
            config_values=request["config_values"]

        )
        res_data = self.stub.ConfigRobot(configRobotRequest)
        print(res_data)
        return res_data

    def get_robot_state(self, header, request):
        """
        查询机器人参数

        :param request: 配置信息
        :param header: robot基本信息
        :return:
        """

        getRobotStateRequest = robot_config_api_pb2.GetRobotStateRequest(
            common_req_info=tools.convert_header(header),
            config_names=request["config_names"]
        )
        res_data = self.stub.GetRobotState(getRobotStateRequest)
        print(res_data)
        return res_data

    def config_record_media(self, header, request):
        """
        视频录制设置

        :param request: 配置信息
        :param header: robot基本信息
        :return:
        """
        configRecordMediaRequest = robot_config_api_pb2.ConfigRecordMediaRequest(
            common_req_info=tools.convert_header(header),
            start_param=request["start_param"],
            stop_param=request["stop_param"]
        )

        if request["start_param"] is not None:
            configRecordMediaRequest["start_param"]=request["start_param"]

        if request["stop_param"] is not None:
            configRecordMediaRequest["stop_param"] = request["stop_param"]

        res_data = self.stub.ConfigRecordMedia(configRecordMediaRequest)
        print(res_data)
        return res_data

    def config_asr(self, header, request):
        """
        控制ARS开/关

        :param request: 配置信息
        :param header: robot基本信息
        :return:
        """

        configAsrRequest = robot_config_api_pb2.ConfigAsrRequest(
            common_req_info=tools.convert_header(header),
            enable_asr=request["enable_asr"]
        )

        res_data = self.stub.ConfigAsr(configAsrRequest)
        print(res_data)
        return res_data

    def config_fr(self, header, request):
        """
        控制识别功能开/关

        :param request: 配置信息
        :param header: robot基本信息
        :return:
        """
        configFrRequest = robot_config_api_pb2.ConfigFrRequest(
            common_req_info=tools.convert_header(header),
            enable_fr=request["enable_fr"]
        )

        res_data = self.stub.ConfigFr(configFrRequest)
        print(res_data)
        return res_data

    def config_face_cam(self, header, request):
        """
        控制机器人本体摄像头识别功能开/关

        :param request: 配置信息
        :param header: robot基本信息
        :return:
        """

        configFaceCamRequest = robot_config_api_pb2.ConfigFaceCamRequest(
            common_req_info=tools.convert_header(header),
            open_face_cam=request["open_face_cam"],
            camera_index=request["camera_index"]
        )

        res_data = self.stub.ConfigFaceCam(configFaceCamRequest)
        print(res_data)
        return res_data

    def config_screen_shot(self, header, request):
        """
        控制短视频与截图录制

        :param request: 配置信息
        :param header: robot基本信息
        :return:
        """
        CameraConfigs = []
        camera_configs = request["camera_configs"]

        for camera_config in camera_configs:
            name = camera_config["name"]
            grabber = camera_config["grabber"]
            CameraConfig = robot_config_api_pb2.CameraConfig(
                name=name,
                grabber=grabber
                # ,
                # screen_shot=screenShot,
                # short_video=shortVideo,
                # cache=cache_data
            )
            screen_shot = camera_config["screen_shot"]
            if screen_shot is not None:
                CameraConfig.screen_shot = robot_config_api_pb2.ScreenShot(
                    filename=screen_shot["filename"]
                )
            # screenShot = robot_config_api_pb2.ScreenShot(
            #     filename=screen_shot["filename"]
            # )
            short_video = camera_config["short_video"]
            if short_video is not None:
                CameraConfig.short_video = robot_config_api_pb2.ShortVideo(
                    duration=short_video["duration"],
                    filename=short_video["filename"]
                )

            # shortVideo = robot_config_api_pb2.ShortVideo(
            #     duration=short_video["duration"],
            #     filename=short_video["filename"]
            # )
            cache = camera_config["cache"]
            if cache is not None:
                CameraConfig.cache = robot_config_api_pb2.Cache(
                    duration=cache["duration"],
                    enable=cache["enable"]
                )
            # cache_data = robot_config_api_pb2.Cache(
            #     duration=cache["duration"],
            #     enable=cache["enable"]
            # )

            CameraConfigs.append(CameraConfig)

        configScreenShotRequest = robot_config_api_pb2.ConfigScreenShotRequest(
            common_req_info=tools.convert_header(header),
            camera_configs=CameraConfigs
        )

        res_data = self.stub.ConfigScreenShot(configScreenShotRequest)
        print(res_data)
        return res_data

