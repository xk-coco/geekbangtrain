#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/26 23:19
# @File    : p1_inheritance.py

# 父类
class People:
    def __init__(self):
        self.gene = 'XY'

    def walk(self):
        print('I can walk.')


# 子类
class Man(People):
    def __init__(self, name):
        self.name = name

    def work(self):
        print("work hard")


class Women(People):
    def __init__(self, name):
        self.name = name

    def shopping(self):
        print("buy buy buy")


p1 = Man('Adam')
p2 = Women('Eve')

# 问题1：gene有没有被继承？
print(p1.gene)
# AttributeError: 'Man' object has no attribute 'gene' #

# 问题2：People的父类是谁？

# 问题3：能否实现多重层级继承？

# 问题4：能否实现多个父类同时继承？
