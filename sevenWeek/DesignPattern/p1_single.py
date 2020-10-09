#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/28 8:02
# @File    : p1_single.py


# 方法一：使用装饰器实现单例模式
def singletin(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls
        return instances[cls]

    return getinstance


@singletin
class Myclass:
    pass


p1 = Myclass()
p2 = Myclass()
print(id(p1))
print(id(p2))


#############################
# __new__ 与 __init__ 的关系
class Foo(object):
    def __new__(cls, name):
        print(f"trace __new__")
        return super().__new__(cls)

    def __init__(self, name):
        print(f"trace __init__")
        super().__init__()
        self.name = name


bar = Foo('test')
bar.name

# 相当于在执行下面的操作：
bar = Foo.__new__(Foo, 'test')
if isinstance(bar, Foo):
    Foo.__init__(bar, 'test')


# 方法二：以__new__ + object 方式实现单例模式
class Singleton2:  # 针对单线程
    __instance = False  # 私有变量，默认没有被实例化

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance  # 返回实例化对象
        # cls.__instance = object.__new__(cls)  # 实例化
        cls.__instance = super(Singleton2, cls).__new__(cls, *args, **kwargs)  # 或者，这样写
        return cls.__instance


# 多线程的情况如何处理？加锁
# 解决并发，引入带锁版
import threading


class SingletonThreading(object):
    objs = {}
    objs_locker = threading.Lock();

    def __new__(cls, *args, **kwargs):
        if cls in cls.objs:
            return cls.objs[cls]
        cls.objs_locker.acquire()
        try:
            if cls in cls.objs[cls]:
                return cls.objs[cls]  # double check locking
            cls.objs[cls] = object.__new__(cls)
        finally:
            cls.objs_locker.release()

# 利用经典的双检查锁机制，确保了在并发环境下Singleton的正确实现。
# 但这个方案并不完美，至少还有以下两个问题：
# 1、如果Singleton的子类重载了__new__()方法，会覆盖或者干扰Singleton类中__new__()的执行，虽然这种情况出现的概率极小，但不可忽视。
# 2、如果子类有__init__()方法，那么每次实例化该Singleton的时候，__init__()都会被调用到，这显然是不应该的，__init__()只应该
#   在创建实例的时候被调用一次。
# 这两个问题当然可以解决，比如通过文档告知其他程序员，子类化Singleton的时候，请务必记得调用父类的__new__()方法；
# 而第二个问题也可以通过偷偷地替换掉__init__()方法来确保它只调用一次。


# 但是，为了实现一个单例，做大量的、水面之下的工作让人感觉相当不Pythonic。
# 这也引起了Python社区的反思，有人开始重新审视Python的语法元素，发现模块采用的其实是天然的单例的实现方式。
# 1、所有的变量都会绑定到模块。
# 2、模块只初始化一次。
# 3、import机制是线程安全的（保证了在并发状态下模块也只有一个实例）。
# 当我们想要实现一个游戏世界时，只需简单地创建World.py就可以了。