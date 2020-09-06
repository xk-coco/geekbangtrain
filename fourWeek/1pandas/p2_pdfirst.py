#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 12:53
# @File    : p2_pdfirst.py

import pandas as pd
import numpy as np
import matplotlib as plt
import os

pwd = os.path.dirname(os.path.realpath(__file__))
# print(pwd)
# rootPath = os.path.split(pwd)
# print(str(rootPath))
book = os.path.join(f"{pwd}\\..\\..\\testDatafile", 'book_utf8.csv')
print(book)
df = pd.read_csv(book)

# 输出全部内容
print(df)

# 筛选标题为“还行”这一列
print(df['还行'])  # 没有指定表头时默认第一行为表头

# 切片方式筛选，显示前3行
print(df[1:3])

# 增加列名
df.columns = ['star', 'vote', 'shorts']

print(df)

# 显示特定的行和列
print(df.loc[1:3, ['star']])

# 过滤数据
print(df['star'] == '力荐')  # 返回的是False或者True
print(df[df['star'] == '力荐'])  # 返回具体的内容

# 缺失数据过滤
df.dropna()  # Return a new Series with missing values removed.

# 数据聚合
print(df.groupby('star').sum())

# 创建新列
star_to_number = {
    '力荐': 5,
    '推荐': 4,
    '还行': 3,
    '较差': 2,
    '很差': 1
}
df['new_star'] = df['star'].map(star_to_number)

print(df)

# 过滤出中评以上的数据（评分大于等于3）
print(df['new_star'] >= 3)  # 返回的是False或者True
print(df[df['new_star'] >= 3])  # 返回具体的内容
