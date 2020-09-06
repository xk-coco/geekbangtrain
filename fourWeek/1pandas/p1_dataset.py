#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 7:58
# @File    : p1_dataset.py


from sklearn import datasets  # 引入数据集

# 鸢尾花数据集
iris = datasets.load_iris()
x, y = iris.data, iris.target

# 查看特征
print(iris.feature_names)

# 查看标签
print(iris.target_names)

# 按照3比1的比例划分训练集和测试集
from sklearn.model_selection import train_test_split

x_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
print(x_train)
print(X_test)
print(y_train)
print(y_test)

# load_xxx 各种数据集
# load_boston Boston房屋价格 回归
# load_digit 手写体 分类
# load_iris 鸢尾花 分类聚类
