#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 13:27
# @File    : p8_semaphore.py


import time
import threading

# 信号量：内部实现一个计数器，占用信号量的线程数超过指定值时阻塞
num = 0
semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行


def run(n):
    semaphore.acquire()
    print(f"run the thread: {n}")
    time.sleep(2)
    semaphore.release()


for i in range(20):
    t = threading.Thread(target=run, args=(i,))
    t.start()
