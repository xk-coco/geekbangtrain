#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 7:46
# @File    : p2_class.py


import threading
import time


class MyThread(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    # 一定要重写run
    def run(self) -> None:
        print("Current task: ", self.n)
        time.sleep(2)


if __name__ == '__main__':
    t1 = MyThread("Thread 1")
    t2 = MyThread("Thread 2")

    t1.start()
    t2.start()

    # 将t1,t2加入到主线程中
    t1.join()
    t2.join()
