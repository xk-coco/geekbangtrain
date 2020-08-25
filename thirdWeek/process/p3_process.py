#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 7:50
# @File    : p3_process.py

from multiprocessing import Process


# 参数
# multiprocessing.Process(group=None,target=None,name=None,args=(),kwargs={})
# - group：分组，实际上很少使用
# - target：表示调用对象，可以传入方法的名称（函数）
# - name：别名，相当于给这个进程取一个名字
# - args：表示被调用对象的位置参数元组，比如target是函数a，有两个参数m,n，那么args就可以传入(m,n)
# - kwargs：表示调用对象的字典


def f(name):
    print(f'hello {name}')


if __name__ == '__main__':
    # 注意：是函数f，参数是元组，不是字符串
    p = Process(target=f, args=('john',))
    p.start()
    p.join()
    # join([timeout])表示等待子进程结束
    # 如果可选参数[timeout]是None（默认值），则该方法被阻塞，直到调用join()方法的进程终止。
    # 如果timeout是一个正数，则最多阻塞timeout秒。
    # 请注意，如果进程终止或方法超时，则该方法返回None，检查进程的exitcode以确定它是否终止。
    # 一个进程可以合并多次，但进程无法进入自身，因为会导致死锁，尝试在启动进程之前合并进程是错误的。
