#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
接受ASR语音文字数据的服务
"""
from protopb.serviceapp import recognizeSpeech_pb2, recognizeSpeech_pb2_grpc
from protopb.common import common_pb2
from concurrent import futures
from src.rdk.speechserver.SpeechService import SpeechService
import grpc


class SpeechServer():

    def __init__(self, host_port, callback):
        self.callback = callback
        self.host_port = host_port

    def StartServer(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        recognizeSpeech_pb2_grpc.add_SpeechServicer_to_server(SpeechService(self.callback), server)
        server.add_insecure_port(self.host_port)
        server.start()
        print("server start")
        server.wait_for_termination()
        print("terminate")












