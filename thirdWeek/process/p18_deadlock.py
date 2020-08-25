#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 13:47
# @File    : p18_deadlock.py

from multiprocessing import Process, Queue


def f(q: Queue):
    q.put('X' * 1000000)


if __name__ == '__main__':
    queue = Queue()
    p = Process(target=f, args=(queue,))
    p.start()
    p.join()  # this deadlocks
    obj = queue.get()

# 如何修复？交换最后两行即可
