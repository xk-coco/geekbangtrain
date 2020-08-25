#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/13 7:22
# @File    : p5_debug.py


import os
from multiprocessing import Process
import multiprocessing


def debug_info(title):
    print('-' * 20)
    print(title)
    print(f"模块名称: {__name__}")
    print('父进程', os.getppid())
    print(f"子进程: {os.getpid()}")
    print('-' * 20)


def f(name):
    debug_info('function f')
    print(f"hello,{name}")


if __name__ == '__main__':
    debug_info('main')
    p = Process(target=f, name='Child Process 1', args=('Bob',))
    p.start()
    # 阻塞2秒
    # p.join(2)

    for p in multiprocessing.active_children():
        print(f"子进程名称： {p.name}   id:{str(p.pid)}")
    print("进程结束")
    print(f"CPU核心数量：{str(multiprocessing.cpu_count())}")
    p.join()
