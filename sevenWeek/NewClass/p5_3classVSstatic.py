#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 12:43
# @File    : p5_3classVSstatic.py


class Foo:
    """类的三种语法形式"""

    def instance_method(self):
        print("是类的实例方法，只能被实例对象调用")

    @staticmethod
    def static_method():
        print("是静态方法")

    @classmethod
    def class_method(cls):
        print("是类方法")


if __name__ == '__main__':
    foo = Foo()
    foo.instance_method()
    foo.static_method()
    foo.class_method()
    print("-----------------------------")
    Foo.static_method()
    Foo.class_method()
