#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 7:57
# @File    : p17_pvt.py

# precess VS thread
import multiprocessing as mp


def job(q):  # CPU计算密集型
    res = 0
    for i in range(1000000):
        res += i + i ** 2 + i ** 3
    q.put(res)


# 多核
def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:', res1 + res2)


# 创建多线程mutithread
# 接下来创建多线程程序，创建多线程和多进程有很多相似的地方。
# 首先import threading然后定义multithread()完成同样的任务
import threading as td


def multithread():
    q = mp.Queue()  # thread可放入Process同样的Queue中
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print("multithread: ", res1 + res2)


# 创建普通函数
def normal():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i + i ** 2 + i ** 3
    print('normal: ', res)


# 在上面例子中我们建立了两个进程或线程，均对job()进行了两次运算，
# 所以在normal()中我们也让它循环两次
# 运行时间
import time

if __name__ == '__main__':
    st = time.time()
    normal()
    str1 = time.time()
    print(f"normal time: {str1 - st}")
    multithread()
    str2 = time.time()
    print(f"multithread time: {str2 - str1}")
    multicore()
    print(f"multicore time: {time.time() - str2}")
