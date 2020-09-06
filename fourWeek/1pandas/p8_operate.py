#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 13:20
# @File    : p8_operate.py


import pandas as pd

df = pd.DataFrame({
    "A": [5, 3, None, 4],
    "B": [None, 2, 4, 3],
    "C": [4, 3, 8, 5],
    "D": [5, 4, 2, None]
})

# 算术运算
# 两列之间的加减乘除
print(df)
print(df['A'] + df['C'])

# 任意一列加/减一个常数值，这一列的所有值都加/减这个常数值
print(df['A'] + 5)

# 比较运算
print(df[df['A'] > df['C']])

# count非空值每列计数
print(df.count())
# count非空值每行计数
print(df.count(axis=1))

# 非空值每列求和
print(df.sum())
print(df['A'].sum())

# mean求均值
# max求最大值
# min求最小值
# median求中位数
# mode求众数
# var求方差
# std求标准差
