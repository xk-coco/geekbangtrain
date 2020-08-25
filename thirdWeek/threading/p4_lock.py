#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 8:00
# @File    : p4_nolock.py


import threading
import time

num = 0
mutex = threading.Lock()


class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(1):  # 加锁
            print(f"thread name: {threading.Thread.getName(self)}")
            num += 1
            print(f"num value is {num}")
        mutex.release()  # 解锁


if __name__ == '__main__':
    for i in range(5):
        t = MyThread()
        t.start()
    print("main thread stop")
