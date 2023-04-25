# coding=utf-8
"""
@ FILE NAME:   urls.py
@ HISTORY:     2023/4/25 16:03   [Z10]
@ DESC:        
"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
