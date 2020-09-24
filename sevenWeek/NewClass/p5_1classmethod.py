#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 1:04
# @File    : p5_1classmethod.py

# 让实例的方法成为类的方法


class Kls1:
    bar = 1

    def foo(self):
        print("I'm foo")

    # 使用类属性、方法
    @classmethod
    def class_foo(cls):
        print(cls.bar)
        print(cls.__name__)
        cls().foo()
        # cls.foo()  # 有什么区别？会报错，因为是类直接调用，不是对象调用，提示缺少self


#####################################
class Story:
    snake = 'Python'

    def __init__(self, name):
        self.name = name

    # 类的方法
    @classmethod
    def get_apple_to_eve(cls):
        return cls.snake


##########################################
def pre_name(obj, name):
    f_name, s_name = name.split('-')
    return obj(f_name, s_name)


class Kls2:
    def __init__(self, f_name, s_name):
        self.first_name = f_name
        self.second_name = s_name

    def print_name(self):
        print(f'first name is {self.first_name}')
        print(f'second name is {self.second_name}')


class Kls3:
    def __init__(self, f_name, s_name):
        self.first_name = f_name
        self.second_name = s_name

    def print_name(self):
        print(f'first name is {self.first_name}')
        print(f'second name is {self.second_name}')

    @classmethod
    def pre_name(cls, name):
        f_name, s_name = name.split('-')
        return cls(f_name, s_name)


##########################################
class Fruit:
    total = 0

    @classmethod
    def print_total(cls):
        print(cls.total)
        print(Fruit.total)
        print(id(Fruit.total))
        print(id(cls.total))

    @classmethod
    def set_total(cls, value):
        print(f'calling {cls} ,{value}')
        cls.total = value


class Apple(Fruit):
    pass


class Orange(Fruit):
    pass


if __name__ == '__main__':
    # Kls1.class_foo()
    s = Story('anyone')
    # get_apple_to_eve 是bound（绑定）方法，查找顺序是先找s的__dict__是否有get_apple_to_eve，如果没有，查类Story
    print(s.get_apple_to_eve)

    # 类和实例都可以使用类方法
    print(s.get_apple_to_eve())
    print(Story.get_apple_to_eve())

    me = Kls2('wilson', 'yin')
    me.print_name()

    ### 问题：输出改为 wilson-yin或wilson:yin
    # 解决方法：
    #   1、修改 __init__()
    #   2、增加 __new__() 构造方法
    #   3、增加 提前处理函数（可以放入类中，定义为classmethod）

    mp = pre_name(Kls2, 'wilson-yin')
    mp.print_name()

    mk3 = Kls3.pre_name('wilson-yin')
    mk3.print_name()

    print("Fruit:")

    Apple.set_total(100)
    # calling <class '__main__.Apple'> ,100
    Orange.set_total(200)
    # calling <class '__main__.Orange'> ,200

    org = Orange()
    org.set_total(300)  # 会修改原有值
    # calling <class '__main__.Orange'> ,300

    Apple.print_total()
    Orange.print_total()
