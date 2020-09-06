#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/5 10:40
# @File    : p10_multitable.py


import pandas as pd
import numpy as np

group = ['x', 'y', 'z']
data1 = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 10)],
    "age": np.random.randint(15, 50, 10)
})

data2 = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 10)],
    "salary": np.random.randint(5, 50, 10)
})

data3 = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 10)],
    "age": np.random.randint(15, 50, 10),
    "salary": np.random.randint(5, 50, 10)
})

# 一对一拼接，拼接使用merge
print(pd.merge(data1, data2))

print(data2)
print(data3)

# 多对一
print(pd.merge(data3, data2, on='group'))

# 多对多连接
print(pd.merge(data3, data2))

# 连接键类型，解决没有公共列问题
print(pd.merge(data3, data2, left_on='age', right_on='salary'))

# 连接方式
# 内连接，不指明连接方式，默认是内连接
print(pd.merge(data3, data2, on='group', how='inner'))
# 左连接 left
# 右连接 right
# 外连接 outer

# 纵向连接，concat常用
print(pd.concat([data1, data2]))
