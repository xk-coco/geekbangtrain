#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 10:44
# @File    : p1_mode.py

import jieba

strings = ["我来到北京清华大学", "乒乓球拍卖完了", "中国科学技术大学"]

for stirng in strings:
    result = jieba.cut(stirng, cut_all=False)
    print('Default Mode:' + "/".join(list(result)))

for stirng in strings:
    result = jieba.cut(stirng, cut_all=True)
    print('Full Mode:' + "/".join(list(result)))

result = jieba.cut("钟南山院士接受采访新冠不会二次爆发")  # 默认模式是精确模式
print('/'.join(list(result)))
# “新冠”没有在词典中，但是被Viterbi算法识别出来了

result = jieba.cut_for_search('小明硕士毕业于中国科学院计算所，后在日本东京大学深造')  # 搜索引擎模块
print('Search Mode: ' + "/".join(list(result)))
