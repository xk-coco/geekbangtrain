#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 13:44
# @File    : p10_timer'.py

# 定时器：指定n秒后执行
from threading import Timer


def hello():
    print("Hello,World")


t = Timer(3, hello)  # 表示3秒后执行hello函数
t.start()
