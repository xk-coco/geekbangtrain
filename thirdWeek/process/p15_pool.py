#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/14 16:17
# @File    : p15_pool.py

# Pool类表示一个工作进程池
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程

from multiprocessing.pool import Pool
from time import sleep, time
import random
import os


def run(name):
    print(f"{name}子进程开始，进程ID：{os.getpid()}")
    start = time()
    sleep(random.choice([1, 2, 3, 4]))
    end = time()
    print(f"{name}子进程结束，进程ID：{os.getpid()}.耗时{(end - start):0.2f}")


if __name__ == '__main__':
    print("父进程开始")
    # 创建多个进程，表示可以同时执行的进程数量，默认大小是CPU的核心数
    # 如果 processes 为 None，则使用 os.cpu_count() 返回的值
    p = Pool(4)
    for i in range(10):
        # 创建异步进程， 放入进程池统一管理
        p.apply_async(run, args=(i,))
        # p.apply(run, args=(i,))  # 同步进程
    # 如果用的是进程池，在调用join()之前必须要先close()或termin ate()
    # 在close()之后不能在继续网进程池添加新的进程
    p.close()
    p.join()
    print("父进程结束")
    p.terminate()

# close():如果我们用的是进程池，在调用join()之前必须先close()，并且在close()之后不能再继续往进程池添加新的进程
# join():进程池对象调用join，会等待进程池中所有的子进程结束完毕再去结束父进程
# terminate():一旦运行到此步，不管任务是否完成，立即终止。
