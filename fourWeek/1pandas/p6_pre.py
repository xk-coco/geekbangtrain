#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 14:52
# @File    : p6_pre.py

import pandas as pd
import numpy as np

x = pd.Series([1, 2, np.nan, 3, 4, 5, 6, np.nan, 8])
# 校验序列中是否存在缺失值
print(x.hasnans)

# 将缺失值填充为平均值
y = x.fillna(value=x.mean())  # 填充了之后需要赋予给新的变量进行操作
print(x)
print(y)

df3 = pd.DataFrame({
    'A': [5, 3, None, 4],
    'B': [None, 2, 4, 3],
    'C': [4, 3, 8, 5],
    'D': [5, 4, 2, None]
})

print(df3)
print(df3.isnull().sum())  # 统计缺失值

print(df3.ffill())  # 用上一行填充
print(df3.ffill().ffill(axis=1))  # 用前一列填充

# 缺失值删除
print(df3.info())
print(df3.dropna())

# 填充缺失值为指定值
print(df3.fillna('无'))
