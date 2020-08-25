#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 13:15
# @File    : p7_condition.py

# 条件锁：该机制会使线程等待，只有满足某条件时，才释放n个线程

import threading


def condition():
    ret = False
    r = input(">>>")
    if r == "yes":
        ret = True
    return ret


def func(conn: threading.Condition, i):
    conn.acquire()
    conn.wait_for(condition)  # 这个方法接收一个函数的返回值
    print(i + 100)
    conn.release()


if __name__ == '__main__':
    c = threading.Condition()
    for i in range(10):
        t = threading.Thread(target=func, args=(c, i,))
        t.start()
