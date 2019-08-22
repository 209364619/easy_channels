"""
time: 2019/8/22 
author：hph
"""
from channels.generic.websocket import WebsocketConsumer
import json
class WsConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = 'from server: ' + text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        },ensure_ascii=False))