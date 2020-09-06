#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 11:01
# @File    : p2_keyword.py

import jieba.analyse

text = '机器学习，需要一定的数学基础，需要掌握的数学基础知识特别多，如果从头到尾开始学，估计大部分人来不及，我建议先学习最基础的数学知识'
# 基于TF-IDF算法进行关键词抽取
tfidf = jieba.analyse.extract_tags(
    text,
    topK=5,  # 权重最大的topK个关键词
    withWeight=True  # 返回每个关键字的权重值
)

# 基于TextRank算法进行关键字抽取
textrank = jieba.analyse.textrank(
    text,
    topK=5,  # 权重最大的topK个关键字
    withWeight=False  # 返回每个关键字的权重值
)

print(tfidf)

import pprint

pprint.pprint(tfidf)
pprint.pprint(textrank)

# 经过比较可知，TF-IDF算法更准确一点
