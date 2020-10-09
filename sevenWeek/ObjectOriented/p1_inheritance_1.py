#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/26 23:19
# @File    : p1_inheritance.py

# 父类
class People:
    def __init__(self, name):
        self.gene = 'XY'
        # 假设人人都有名字
        self.name = name

    def walk(self):
        print('I can walk.')


# 子类
class Man(People):
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        print("work hard")


class Women(People):
    def __init__(self, name):
        super().__init__(name)

    def shopping(self):
        print("buy buy buy")


p1 = Man('Adam')
p2 = Women('Eve')

# 问题1：gene有没有被继承？
print(p1.gene)
# Output:XY，表示已经继承

# 问题2：People的父类是谁？
# object 与 type
print('object', object.__class__, object.__bases__)
print('type', type.__class__, type.__bases__)


# type元类由type自身创建，object类由元类type创建
# type类继承了object类


# 问题3：能否实现多重层级继承？

# 问题4：能否实现多个父类同时继承？
class son(Man, Women):
    pass

# 新的问题：继承顺序？
# 钻石继承
