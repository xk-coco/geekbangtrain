#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 14:08
# @File    : p11_queue.py


import queue

q = queue.Queue(5)
q.put(111)
q.put(222)
q.put(333)

print(q.get())
q.task_done()  # 每次从queue中get一个数据之后，当处理好相关问题，最后调用该方法
# 以提示q.join()是否停止阻塞，让线程继续执行或者退出
print(q.qsize())
print(q.empty())
print(q.full())

###########################

import queue
import threading
import random
import time

writelock = threading.Lock()


class Producer(threading.Thread):
    def __init__(self, q: queue, con: threading.Lock, name):
        super(Producer, self).__init__()
        self.q = q
        self.con = con
        self.name = name
        print(f"Process {self.name} Started")

    def run(self) -> None:
        while True:
            global writelock
            self.con.acquire()  # 获取锁对象

            if self.q.full():  # 队列满
                with writelock:
                    print("Queue is full, producer wait")
                self.con.wait()  # 等待资源
            else:
                value = random.randint(0, 10)
                with writelock:
                    print(f"{self.name} put value {self.name} {str(value)} in queue.")
                self.q.put((f"{self.name}:{str(value)}"))  # 放入队列
                self.con.notify()  # 通知消费者
                time.sleep(1)
        self.con.release()


class Consumer(threading.Thread):
    def __init__(self, q: queue, con, name):
        super(Consumer, self).__init__()
        self.q = q
        self.name = name
        self.con = con
        print(f"Consumer {self.name} Started.")

    def run(self) -> None:
        while True:
            global writelock
            self.con.acquire()
            if self.q.empty():  # 队列空
                with writelock:
                    print("Queue is empty, consumer wait.")
                self.con.wait()  # 等待资源
            else:
                value = self.q.get()
                with writelock:
                    print(f"{self.name} get value {value} from queue")
                self.con.notify()  # 通知生产者
                time.sleep(1)
        self.con.release()


if __name__ == '__main__':
    q = queue.Queue(10)
    con = threading.Condition()  # 条件变量锁
    p1 = Producer(q, con, "P1")
    p1.start()
    p2 = Producer(q, con, "P2")
    p2.start()
    c1 = Consumer(q, con, "C1")
    c1.start()

# 练习使用列表实现队列
