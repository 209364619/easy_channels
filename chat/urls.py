"""
time: 2019/8/22 
author：hph
"""
from django.urls import path
from chat import views
urlpatterns = [
    path('',views.index)
]