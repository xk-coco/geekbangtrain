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
        print(f"__getattribute__ called item: {item}")
        print("存在属性，则返回对应的值，否则报AttributeError错误")
        # return super().__getattribute__(item)  # 有属性，获取值的时候在前面返回一些提示
        return self.__getattribute__(item)


h1 = Human2()
print(h1.age)  # 存在的属性返回值
print(h1.noattr)  # 不存在的属性返回AttributeError

# 思考：为什么使用super()不使用self？
