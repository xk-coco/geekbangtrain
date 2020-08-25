#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 13:37
# @File    : p9_event.py

# 事件：定义一个flag，set设置flag为True，clear设置flag为False
import threading


def func(e, i):
    print(i)
    e.wait()  # 检查当前event是什么状态，如果是红灯，则阻塞，如果是绿灯则继续往下执行。默认是红灯
    print(i + 100)


event = threading.Event()
for i in range(10):
    t = threading.Thread(target=func, args=(event, i))
    t.start()

event.clear()  # 主动将状态设置为红灯
inp = input(">>>")
if inp == "1":
    event.set()  # 主动将状态设置为绿灯

# 练习：使用redis实现分布式锁
