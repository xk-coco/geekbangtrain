#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/13 8:02
# @File    : p7_var.py


# 全局变量在多个进程中不能共享
# 在子进程中修改全局变量对父进程中的全局变量没有影响
# 因为父进程在创建子进程时对全局变量做了一个备份
# 父进程中的全局变量与子进程的全局变量完全是不同的两个变量
# 全局变量在多个进程中不能共享

from multiprocessing import Process
from time import sleep

num = 100


def run():
    print("子进程开始")
    global num
    num += 1
    print(f"子进程num:{num}")
    print("子进程结束")


if __name__ == '__main__':
    print("父进程开始")
    p = Process(target=run)
    p.start()
    p.join()

    # 在子进程中修改全局变量对父进程的全局变量没有影响（也是和线程的区别）
    print(f"父进程num:{num}")
