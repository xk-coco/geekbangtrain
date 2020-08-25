#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 7:38
# @File    : p1_func.py


import threading
import time


# 这个函数名可随便定义
def run(n):
    print("current task: ", n)
    time.sleep(3)


if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=("thread 1",))
    t2 = threading.Thread(target=run, args=("thread 2",))
    t1.start()
    # t1.join()   # 挂起，同步
    t2.start()

# 调用方
# 阻塞 得到结果之前，线程会被挂起
# 非阻塞 不能立即得到结果，不会阻塞线程

# 被调用方
# 同步 得到结果之前，调用不会返回
# 异步 请求发出后，调用立即返回、没有返回结果，实际结果通过回调函数得到
