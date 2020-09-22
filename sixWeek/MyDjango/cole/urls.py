#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 1:01
# @File    : urls.py

from django.urls import path, re_path, register_converter
from . import views, converters

register_converter(converters.IntConverter, 'myint')
register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.index, name='index'),

    ### 带变量的URL
    path('<int:year>', views.year),  # 只接收整数，其他类型返回404
    path('<str:name>/<int:year>', views.nameandyear),

    ### 正则匹配
    re_path('(?P<year>\d{4}).html', views.myyear, name='urlyear'),  # (?P<name>...) 分组除原有编号外，再加一个别名alias

    ### 自定义过滤器
    # path('<myint:year>', views.year)  # 从上到下匹配，一旦匹配到，即停止匹配

    path('books', views.books)

]
