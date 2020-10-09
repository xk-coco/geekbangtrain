#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 0:09
# @File    : p4_overload.py


class Klass(object):
    def A(self):
        pass

    def A(self, a, b):
        print(f"{a} and {b}")


inst = Klass

# Python没有实现重载
inst.A()
# Output:TypeError: A() missing 3 required positional arguments: 'self', 'a', and 'b'
