#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
自然语言识别接口
"""

import grpc
from protopb.common import common_pb2
from protopb.nlu import nlu_pb2, nlu_pb2_grpc
from src.rdk.tools import tools


class NluService(object):

    def __init__(self, grpc_url, authority):
        print("NluService init--")
        self.grpc_url = grpc_url
        # channel = grpc.insecure_channel(grpc_url, options=[('grpc.default_authority', 'harix-skill-nlu.harix-allinone3')])
        channel = grpc.insecure_channel(grpc_url,
                                        options=[('grpc.default_authority', authority)])
        self.stub = nlu_pb2_grpc.NLUStub(channel)

    def nlu_detect(self, header, request):
        common_req_info = tools.convert_header(header)
        text_request = nlu_pb2.TextRequest(
            common_req_info=common_req_info,
            body=request
        )
        res_data = self.stub.Detect(text_request)
        return res_data







