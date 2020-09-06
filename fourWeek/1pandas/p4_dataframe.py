#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 14:17
# @File    : p4_dataframe.py


import pandas as pd

# 列表创建dataframe
df1 = pd.DataFrame(['a', 'b', 'c', 'd'])
print(df1)

# 嵌套列表创建dataframe
df2 = pd.DataFrame([
    ['a', 'b'],
    ['c', 'd']
])
print(df2)

# 自定义列索引
df2.columns = ['one', 'two']
# 自定义行索引
df2.index = ['first', 'second']

print(df2)
# 可以在创建是直接指定行、列索引：DataFrame([...],columns='...',index='...')

# 查看所有
print(df2.columns)
print(df2.index)
print(df2.values)
print(type(df2.values))  # <class 'numpy.ndarray'>
# 转换为list
print(df2.values.tolist())
