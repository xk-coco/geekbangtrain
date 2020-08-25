#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/13 14:04
# @File    : p8_queue2.py


from multiprocessing import Process, Queue
import os, time


def write(q):
    print(f"启动write子进程：{os.getpid()}，父进程是{os.getppid()}")
    for i in ["A", "B", "C", "D"]:
        q.put(i)  # 写入队列
        time.sleep(1)
    print(f"结束write子进程：{os.getpid()}，父进程是{os.getppid()}")


def read(q):
    time.sleep(0.5)
    print(f"启动read子进程：{os.getpid()}，父进程是{os.getppid()}")
    while True:  # 阻塞，等待获取write的值
        value = q.get(True)
        print(value)

    print(f"结束read子进程：{os.getpid()}，父进程是{os.getppid()}")  # 不会执行


if __name__ == '__main__':
    # 父进程创建队列，并传递给子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()

    pw.join()
    # pr进程是一个死循环，无法等待其结束，只能强行结束
    # 写进程结束了，所以读进程也可以结束了
    pr.terminate()
    print(f"父进程{os.getpid()}结束")
