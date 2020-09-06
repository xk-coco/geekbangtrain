#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/28 7:49
# @File    : p7_adjust.py


import pandas as pd

df = pd.DataFrame({
    'A': [5, 3, None, 4],
    'B': [None, 2, 3, 4],
    'C': [4, 3, 8, 5],
    'D': [5, 4, 2, None]
})

print(df)

# 列的选择，多个列要使用列表
print(df[['A', 'C']])  # 选择的列是新值，不会改变原有的值

# 某几列
print(df.iloc[:, [0, 2]])  # :表示所有行列，获取第1和第3列

# 行选择
print(df.loc[[0, 2]])  # 选择第1行和第3行
print(df.loc[0:2])  # 选择第1行到第3行

# 比较
print(df[(df['A'] < 5) & (df['C'] < 4)])

# 数值替换

# 一对一替换
# 用于单个异常值处理
print(df['C'].replace(4, 40))

import numpy as np

print(df.replace(np.NaN, '无'))

# 多对一的替换
print(df.replace([4, 5, 8], 1000))

# 多对多替换
print(df.replace({4: 500, 5: 500, 8: 800}))

# 排序，按照指定列降序排列
print(df.sort_values(by=['A'], ascending=False))

# 多列排序
print(df.sort_values(by=['A', 'C'], ascending=[True, False]))

# 删除
# 删除列
print(df.drop('A', axis=1))

# 删除行
print(df.drop(3, axis=0))

# 删除特定行
print(df[df['A'] < 4])

# 行列互换
print(df.T)
print(df.T.T)

# 索引重塑（数据透视表）
df2 = pd.DataFrame(
    [
        ['a', 'b', 'c'],
        ['d', 'e', 'f']
    ],
    columns=['one', 'two', 'three'],
    index=['first', 'second']
)
print(df2)
print(df2.stack())
print(df2.unstack())
print(df2.stack().reset_index())
