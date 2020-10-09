#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 7:44
# @File    : p7_1descraptor.py


class Desc:
    """
    通过打印来展示描述符的访问流程
    """

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f"__get__{instance}{owner}")
        return self.name

    def __set__(self, instance, value):
        print(f"__set__{instance}{value}")
        self.name = value

    def __delete__(self, instance):
        print(f"__delete__{instance}")
        del self.name


class MyObj:
    a = Desc('aaa')
    b = Desc('bbb')


my_object = MyObj()
print(my_object.a)

my_object.a = 456
print(my_object.a)
