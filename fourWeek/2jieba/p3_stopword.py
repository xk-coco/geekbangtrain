#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 11:01
# @File    : p2_keyword.py

import jieba.analyse

text = '机器学习，需要一定的数学基础，需要掌握的数学基础知识特别多，如果从头到尾开始学，估计大部分人来不及，我建议先学习最基础的数学知识'
stop_words = r'./extra_dict/stop_words'
# stop_words 的文件格式是文本文件，每行一个词语
jieba.analyse.set_stop_words(stop_words)

# 基于TextRank算法进行关键字抽取
textrank = jieba.analyse.textrank(
    text,
    topK=5,  # 权重最大的topK个关键字
    withWeight=False  # 返回每个关键字的权重值
)

import pprint

pprint.pprint(textrank)
