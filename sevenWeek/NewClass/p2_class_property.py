#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/23 23:13
# @File    : p2_class_property.py

# GOD

class Human:
    # 静态字段，属于类
    live = True

    def __init__(self, name):  # self指实例本身，可以更改为任意的字符
        # 普通字段
        self.name = name


man = Human('adam')
womam = Human('Eve')

# 查看类属性
print(Human.__dict__)
print(Human.__dict__.items())

# 查看对象（实例）属性
print(man.__dict__)

# 引用类属性后
man.live = False
print(man.__dict__)
print(Human.__dict__)

# 类也是对象，可以赋值给变量
c = Human
print(c.__class__)

# 可以为类添加静态属性
Human.newAttr = 1
print(dir(Human))
print(Human.__dict__)

setattr(list, 'newAttrl', 'value')
