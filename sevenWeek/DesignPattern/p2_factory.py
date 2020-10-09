#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/8 10:37
# @File    : p2_factory.py


class Human(object):
    def __init__(self):
        self.name = None
        self.gender = None

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender


class Man(Human):
    def __init__(self, name):
        print(f"Hi,Man {name}")


class Woman(Human):
    def __init__(self, name):
        print(f"Hi,Woman {name}")


### 简单工厂模式
class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Man(name)
        elif gender == 'F':
            return Woman(name)
        else:
            pass


if __name__ == '__main__':
    factory = Factory()
    person = factory.getPerson('Admin', 'M')


### 类工厂模式：返回在函数内动态创建的类
def factory2(func):
    class klass: pass

    # setattr需要三个参数：对象、key、value
    print(func)
    setattr(klass, func.__name__, func)
    ### 如果想创建类方法？
    # setattr(klass, func.__name__, classmethod(func))
    return klass


def say_foo(self):
    print("bar")


Foo = factory2(say_foo)
foo = Foo()
foo.say_foo()
