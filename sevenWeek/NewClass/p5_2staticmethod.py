#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 12:38
# @File    : p5_2staticmethod.py


import datetime


class Story(object):
    snake = 'Python'

    def __init__(self, name):
        self.name = name

    # 静态方法
    @staticmethod
    def god_come_go():  # 不包含self、cls参数
        if datetime.datetime.now().month % 2:
            print('god is coming')


if __name__ == '__main__':
    Story.god_come_go()

# 静态方法可以由类直接调用
# 因为不传入self 也不传入 cls ，所以不能使用类属性和实例属性
