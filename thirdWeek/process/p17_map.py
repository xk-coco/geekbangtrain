#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 14:11
# @File    : p17_map.py

# 将map()引入到进程池
# 如果读过Google的那篇大名鼎鼎的论文“MapReduce: Simplified Data Processing on Large Clusters”，你就能大概明白map/reduce的概念。

from multiprocessing import Pool
import time


def f(x):
    return x * x


def addf(t):
    x, y = t
    return x + y


if __name__ == '__main__':
    with Pool(4) as pool:
        print(pool.map(f, range(10)))
        print(pool.map(addf, ((2, 4),)))
        it = pool.imap(f, range(10))
        print(it)
        print(next(it))
        print(next(it))
        print(it.next(timeout=1))
