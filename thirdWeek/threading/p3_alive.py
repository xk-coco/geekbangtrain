#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 7:57
# @File    : p3_alive.py

import threading
import time


def start():
    time.sleep(3)


thread1 = threading.Thread(target=start)
print(thread1.is_alive())
thread1.start()
print(thread1.is_alive())
print(thread1.getName())
thread1.join()

print(thread1.is_alive())
