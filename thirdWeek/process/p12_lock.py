#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/14 7:31
# @File    : p12_nolock.py

# 进程锁Lock
# 不加进程锁，让我们看看没有加进程锁时会产生什么样的结果

import multiprocessing as mp
import time


def job(v, num, l):
    l.acquire()  # 锁住
    for _ in range(5):
        time.sleep(0.1)
        v.value += num  # v.value获取共享变量值
        print(v.value, end="|")
    l.release()  # 线程操作完成后释放


def multicore():
    l = mp.Lock()  # 定义一个进程锁
    v = mp.Value('i', 0)  # 定义共享变量
    p1 = mp.Process(target=job, args=(v, 1, l))
    p2 = mp.Process(target=job, args=(v, 3, l))
    p1.start()
    p1.join(0.1)
    p2.start()
    # p1.join()
    p2.join()


if __name__ == '__main__':
    multicore()

# 加锁之后，看是否冲突？
