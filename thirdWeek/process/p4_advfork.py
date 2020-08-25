#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 8:10
# @File    : p4_advfork.py

from multiprocessing import Process
import time
import os


def run():
    print("子进程开启")
    time.sleep(2)
    print("子进程结束")


if __name__ == '__main__':
    print("父进程开启")
    p = Process(target=run)
    p.start()
    p.join()  # 阻塞
    print("父进程结束")
