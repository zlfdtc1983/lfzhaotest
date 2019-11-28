#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
语音识别接口
"""

import grpc
from protopb.common import common_pb2
from protopb.speech import enableSpeech_pb2_grpc, enableSpeech_pb2
from src.rdk.tools import tools


class AsrSubscribe(object):

    def __init__(self, grpc_url):
        print("SpeechService init--")
        self.grpc_url = grpc_url
        channel = grpc.insecure_channel(grpc_url, options=[('grpc.default_authority', 'harix-skill-asr.harix-allinone3')])
        self.stub = enableSpeech_pb2_grpc.EnableSpeechStub(channel)

    def subscribe_asr(self, header, request):

        common_req_info = tools.convert_header(header)
        enable_request = enableSpeech_pb2.EnableRequest(
            common_req_info=common_req_info,
            sub_type=request["sub_type"],
            enable=request["enable"],
            sub_addr=request["sub_addr"]
        )
        res_data = self.stub.enable(enable_request)
        return res_data



