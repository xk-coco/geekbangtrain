#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 11:48
# @File    : p1_snownlp.py


from snownlp import SnowNLP

text = '其实故事本来真的只值三星当初的中篇就足够了但是啊看到最后我又一次被东野叔的反战思想打动了所以就加多一星吧'

s = SnowNLP(text)

# 1、中文分词
print(s.words)

# 2、词性标注（隐马尔可夫模型）
print(list(s.tags))

print("=" * 40)

# 3、情感分析（朴素贝叶斯分类器）
print(s.sentiments)
text2 = '这本书烂透了'
s2 = SnowNLP(text2)
print(s2.sentiments)

# 4、转化为拼音（Trie树）
print(s.pinyin)

# 5、繁体转简体
text3 = '後面這些是繁體字'
s3 = SnowNLP(text3)
print(s3.han)

# 6、提取关键字
print(s.keywords(limit=5))

# 7、信息衡量
print(s.tf)  # 词频越大越重要
print(s.idf)  # 包含此条的文档越少，n越小，idf越大，说明词条t越重要
# 8 训练
from snownlp import seg

# seg.train('data.txt')
# seg.save('seg.marshal')
# 修改snownlp/seg/__init__.py的 data_path 指向新的模型即可
