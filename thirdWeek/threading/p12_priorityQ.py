#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 7:52
# @File    : p12_priorityQ.py

import queue

q = queue.PriorityQueue()

# 每个元素都是元组
# 数字越小，优先级越高
# 同优先级先进先出

q.put((1, 'work'))
q.put((-1, 'life'))
q.put((1, 'drink'))
q.put((-2, 'sleep'))

print(q.get())
print(q.get())
print(q.get())
print(q.get())

# queue.LiFOQueue 后进先出队列，类似堆栈
# q.deque 双向队列
