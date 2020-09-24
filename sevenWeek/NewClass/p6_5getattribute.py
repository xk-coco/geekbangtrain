#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 12:56
# @File    : p6_1getattribute.py


class Human2:
    def __init__(self):
        self.age = 18

    def __getattr__(self, item):
        # 对指定属性做处理：fly属性返回'superman'，其他属性返回None
        self.item = item
        if self.item == 'fly':
            return "superman"


h1 = Human2()
print(h1.age)  # 存在的属性返回值
print(h1.noattr)  # 不存在的属性返回None
print(h1.fly)
