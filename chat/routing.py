"""
time: 2019/8/22 
author：hph
"""
from django.urls import path
from chat.consummer import WsConsumer
websocket_urlpatterns = [
    path('ws/chat/',WsConsumer)
]