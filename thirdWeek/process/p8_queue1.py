#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/13 13:47
# @File    : p8_queue1.py


# Queue类是一个近似queue.Queue的克隆
# 现在有这样一个需求：有两个进程，一个写（write）一个读（read）
# 当写的进程写完某部分后要把数据交给读的进程进行使用

from multiprocessing import Process, Queue
import os


def f(q):
    # 依据block和timeout取自定义写队列的状态
    print(f"进程{os.getpid()}:put,父进程是{os.getppid()}")
    q.put([42, None, 'Hello'])


if __name__ == '__main__':
    q = Queue()  # 一般最好设置一个大小
    p = Process(target=f, args=(q,))
    p.start()
    print(f"进程{os.getpid()}:{q.get()}")  # 依据block和timeout可选项可自定义自己的取队列的状态
    p.join()

# 队列是线程和进程安全的
