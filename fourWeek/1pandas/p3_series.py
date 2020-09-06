#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 13:55
# @File    : p3_series.py


import pandas as pd
import numpy as np

# 从列表创建series
print(pd.Series(['a', 'b', 'c']))
# 0    a
# 1    b
# 2    c
# dtype: object
# 自动创建索引

# 通过字典创建带索引的Series
s1 = pd.Series({'a': 11, 'b': 12, 'c': 13})
# 通过关键字创建带索引的Series
s2 = pd.Series([11, 22, 33], index=['a', 'b', 'c'])
print(s1)
print(s2)

# 获取全部索引
print(s1.index)
# 获取全部值
print(s1.values)

# 查看类型
print(type(s1.values))  # <class 'numpy.ndarray'>
print(np.array(['a', 'b']))
print(type(np.array(['a', 'b'])))

# 转化为列表
print(s1.values.tolist())

# 使用index的好处？

# 取出email
emails = pd.Series(['abc at amazom.com', 'admin1@163.com', 'mat@m.at', 'ab@abc.com'])
import re

pattern = '[A-Za-z0-9._]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,5}'
mask = emails.map(lambda x: bool(re.match(pattern, x)))
print(mask)
print(emails[mask])
