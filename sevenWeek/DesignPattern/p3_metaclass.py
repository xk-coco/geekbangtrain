#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/8 16:35
# @File    : p3_metaclass.py


### 使用type元类创建类
def hi():
    print("Hi, metaclass")


### type的三个参数：类名、父类的元组、类的成员
Foo = type('Foo', (), {'say_hi': hi})
foo = Foo
foo.say_hi()
# 元类type首先是一个类，所以比类工厂的方法更灵活多变，可以自由创建子类来扩展元类的能力

"""
需求：定义一个DelDictValue类，除了具备dict的基本功能，要求具备一个额外的“根据value值来删除key、value”功能
"""


def pop_value(self, dict_value):
    for key in self.keys():
        if self.__getitem__(key) == dict_value:
            self.pop(key)
            break


# 元类要求，必须继承自type
class DelValue(type):
    # 元类要求，必须实现new方法
    def __new__(cls, name, bases, attrs):
        attrs['pop_value'] = pop_value
        return type.__new__(cls, name, bases, attrs)


class DelDictValue(dict, metaclass=DelValue):
    # 在python2的用法(__metaclass__ = DelValue)，在python3不支持
    pass


d = DelDictValue()
