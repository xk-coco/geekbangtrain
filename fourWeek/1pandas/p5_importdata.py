#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 14:32
# @File    : p5_importdata.py

import pandas as pd
import os

pwd = os.path.dirname(os.path.realpath(__file__))
excledir = os.path.join(f"{pwd}\\..\\..\\testDatafile", '1.xlsx')

excel1 = pd.read_excel(excledir)
print(excel1)

# 熟悉数据
# 显示前几行
print(excel1.head(2))

# 行列数量
print(excel1.shape)

# 详细信息
print(excel1.info())
print(excel1.describe())
