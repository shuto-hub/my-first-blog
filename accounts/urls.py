#!/usr/bin/python3
#coding:utf-8
from django.conf.urls import url
from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
path('signup/', views.SignUpView.as_view(),name="signup"),
]