#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 14:43
# @File    : p14_pool.py

import requests
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'http://www.baidu.com',
    'http://www.sina.com.cn',
    'http://www.163.com',
    'http://www.qq.com',
    'http://www.taobao.com',
]

# 开启线程
pool = ThreadPool(4)

# 获取URLs的结果
results = pool.map(requests.get, urls)

# 关闭线程池等待任务完成退出
pool.close()
pool.join()

for i in results:
    print(i.url)
