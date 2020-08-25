#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 8:00
# @File    : p4_nolock.py


import threading
import time

# Lock 普通锁不可嵌套，RLock普通锁可嵌套
mutex = threading.RLock()


class MyThread(threading.Thread):
    def run(self):
        if mutex.acquire(1):  # 加锁
            print(f"thread name: {self.name} get mutex")
            time.sleep(1)
            mutex.acquire()  # 再次获取，嵌套锁
            mutex.release()
        mutex.release()  # 解锁


if __name__ == '__main__':
    for i in range(5):
        t = MyThread()
        t.start()
