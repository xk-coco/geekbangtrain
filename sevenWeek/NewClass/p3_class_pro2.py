#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/23 23:52
# @File    : p3_class_pro2.py

class Human2:
    # 人为约定,单下划线，不要修改
    _age = 0

    # 私有属性，双下划线
    __fly = False

    # 魔术方法，不会自动改名
    # 如：__init__


# 显示object类的所有子类
print(().__class__.__bases__[0].__subclasses__())
print(Human2.__class__.__bases__[0].__subclasses__())

