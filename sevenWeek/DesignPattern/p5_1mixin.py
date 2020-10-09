#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/8 17:55
# @File    : p5_1mixin.py


def mixin(Klass, MixinKlass):
    Klass.__bases__ = (MixinKlass,) + Klass.__bases__


# 定义一个父类
class Fclass(object):
    def text(self):
        print("in FatherClass")


class S1class(Fclass):
    pass


class MixinClass(object):
    def text(self):
        print("in MixinClass")


class S2class(S1class, MixinClass):
    pass


print(f" test1 : S1class MRO: {S1class.mro()}")
s1 = S1class()
s1.text()

mixin(S1class, MixinClass)
print(f"test2 : S1class MRO: {S1class.mro()}")
s1 = S1class()
s1.text()

print(f" test3 : S2class MRO: {S2class.mro()}")
s2 = S2class()
s2.text()
