#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/20 20:34
# @File    : urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index', views.books_short),
]
