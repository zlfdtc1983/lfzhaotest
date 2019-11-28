#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
接受ASR语音文字数据的服务
"""
from protopb.serviceapp import recognizeSpeech_pb2, recognizeSpeech_pb2_grpc
from protopb.common import common_pb2


class SpeechService(recognizeSpeech_pb2_grpc.SpeechServicer):

    def __init__(self, callback):
        self.callback = callback

    def OnRecognizeResult(self, request, context):

        header = {
            "tenant_id": request.common_req_info.tenant_id,
            "user_id": request.common_req_info.user_id,
            "robot_id": request.common_req_info.robot_id,
            "robot_type": request.common_req_info.robot_type,
            "service_code": request.common_req_info.service_code,
            "seq": request.common_req_info.seq
        }

        self.callback(header, request.body)

        common_resp_info = common_pb2.CommonRspInfo(
            err_code=0
        )
        return recognizeSpeech_pb2.RecognitionResponse(
            common_rsp_info=common_resp_info
        )