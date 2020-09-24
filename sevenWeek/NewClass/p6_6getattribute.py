#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 12:56
# @File    : p6_1getattribute.py


class Human2:
    """
    同时存在
    """

    def __init__(self):
        self.age = 18

    def __getattr__(self, item):
        print("Human2: __getattr__")
        return "Error 404, 你请求的参数不存在."

    def __getattribute__(self, item):
        print("Human2: __getattribute__")
        return super().__getattribute__(item)


h1 = Human2()

# 如果同时存在，执行顺序是 __getattribute__ > __getattr__ > __dict__
print(h1.age)  # 存在的属性返回值
print(h1.noattr)  # 不存在的属性返回None
