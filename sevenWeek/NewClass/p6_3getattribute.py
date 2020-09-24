#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 12:56
# @File    : p6_1getattribute.py


class Human2:
    """
    getattribute对任意读取的属性进行截获
    """

    def __init__(self):
        self.age = 18

    def __getattribute__(self, item):
        print("存在属性，则返回，不存在则设置为100并返回")
        try:
            return super().__getattribute__(item)  # 有属性，获取值的时候在前面返回一些提示
        except Exception as e:
            self.__dict__[item] = 100
            return 100


h1 = Human2()
print(h1.age)  # 存在的属性返回值
print(h1.noattr)  # 不存在的属性则设置为100并返回

# 思考：有更简洁的方法吗？
