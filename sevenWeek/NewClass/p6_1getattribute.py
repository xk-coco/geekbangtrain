#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 12:56
# @File    : p6_1getattribute.py

class Human:
    def __init__(self, name):
        self.name = name


h1 = Human('Adam')
h2 = Human('Eve')

print(h1.name)

# 删除实例属性，查询
del h1.name

# attributeError,访问不存在的属性
# 由__getattribute__(self,name)抛出
# h1.name

print(h1.__getattribute__)


# print(h1.__getattribute__())


####################################
class Human2:
    """
    getattribute对任意读取的属性进行截获
    """

    def __init__(self):
        self.age = 18

    def __getattribute__(self, item):
        print(f"__getattribute__ called item: {item}")


h1 = Human2()
print(h1.age)
print(h1.noattr)
