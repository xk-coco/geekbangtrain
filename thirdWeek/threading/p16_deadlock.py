#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 7:36
# @File    : p16_deadlock.py


import time
from concurrent.futures import ThreadPoolExecutor


def wait_on_b():
    time.sleep(5)
    print(b.result)
    return 5


def wait_on_a():
    time.sleep(5)
    print(a.result)
    return 6


executor = ThreadPoolExecutor(max_workers=2)

a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)
