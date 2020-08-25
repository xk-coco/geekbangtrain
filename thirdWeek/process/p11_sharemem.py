#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/13 15:27
# @File    : p11_sharemem.py


# 在进行并发编程时，通常最好尽量避免使用共享状态，使用多个进程时尤其如此
# 如果真的需要使用一些共享数据，那么 multiprocessing 提供了两种方法
# 共享内存 shared memory

# 可以使用 Value 或 Array 将数据存储在共享内存映射中
# 这里的Array和numpy中的不同，它只能是一维的，不能是多维的
# 同样和 Value 一样，需要定义数据形式，否则会报错

from multiprocessing import Process, Value, Array


def f(n, a):
    n.value = 3.1415926
    for i in a:
        a[i] = -a[i]


if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
