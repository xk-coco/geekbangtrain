#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 14:04
# @File    : p16_timeout.py


from multiprocessing import Pool
import time


def f(x):
    return x * x


if __name__ == '__main__':
    with Pool(processes=4) as pool:  # 进程池包含4个进程
        result = pool.apply_async(f, args=(10,))  # 执行一个子进程
        print(result.get(timeout=1))  # 显示执行结果

        result = pool.apply_async(time.sleep, args=(10,))
        print(result.get(timeout=1))  # raises multiprocessing.TimeoutError
