#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/13 7:45
# @File    : p6_class.py

import os
import time
from multiprocessing import Process


class NewProcess(Process):
    def __init__(self, num):
        self.num = num
        super().__init__()

    def run(self) -> None:  # 重写Process类中的run方法（固定格式，一定要重写该方法）
        while True:
            print(f"我是进程: {self.num},我的pid是: {os.getpid()}")
            time.sleep(1)


if __name__ == '__main__':
    for i in range(2):
        p = NewProcess(i)
        p.start()
    # 当不给Process指定target时，会默认调用Process类里的run()方法
    # 这个指定target效果一样的，只是将函数封装进类之后便于理解和调试
