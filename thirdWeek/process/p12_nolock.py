#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/14 7:31
# @File    : p12_nolock.py

# 进程锁Lock
# 不加进程锁，让我们看看没有加进程锁时会产生什么样的结果

import multiprocessing as mp
import time


def job(v, num):
    for _ in range(5):
        time.sleep(0.05)
        v.value += num  # v.value获取共享变量值
        print(v.value, end="|")


def multicore():
    v = mp.Value('i', 0)  # 定义共享变量
    p1 = mp.Process(target=job, args=(v, 1))
    p2 = mp.Process(target=job, args=(v, 3))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    multicore()

# 在上面的代码中，定义了一个共享变量v，两个进程都可以对它进行操作
# 在job()中让v每隔0.05秒输出一次累加num的结果
# 但是在两个进程p1和p2中设置了不同的累加值，看是否冲突？
