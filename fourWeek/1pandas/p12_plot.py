#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/5 11:23
# @File    : p12_plot.py


import pandas as pd
import numpy as np

dates = pd.date_range('20200101', periods=12)
df = pd.DataFrame(np.random.randn(12, 4), index=dates, columns=list('ABCD'))
print(df)

import matplotlib.pyplot as plt

plt.plot(df.index, df['A'], )
plt.show()
plt.plot(df.index, df['A'],
         color='#FFAA00',  # 颜色
         linestyle='--',  # 线条样式
         linewidth=3,  # 线条宽度
         marker='D'  # 点标记
         )
plt.show()

# seaborn其实是在matlabplotlib的基础上进行了更高级的API封装，从而使绘图更容易、更美观
import seaborn as sns

# 绘制散点图
plt.scatter(df.index, df['A'])
plt.show()

# 美化plt
sns.set_style('darkgrid')
plt.scatter(df.index, df['A'])
plt.show()
