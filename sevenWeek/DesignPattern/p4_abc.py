#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/8 17:44
# @File    : p4_abc.py

from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Concrete(Base):
    def foo(self):
        pass


c = Concrete()  # 会报TypeError错误，因为没有实现bar方法
