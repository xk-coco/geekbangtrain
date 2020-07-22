#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 7:51
# @File    : 1a_requests.py

import requests
import lxml.etree

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
header = {'user-agent': user_agent}

doubanurl = "https://movie.douban.com/subject/1292052/"

response = requests.get(doubanurl, headers=header)  # headers参数是为了尽量模拟浏览器的功能
print(f"返回码：{response.status_code}")

# xml化处理
selector = lxml.etree.HTML(response.text)

mylist = []

# 电影名称
film_name = selector.xpath('/html/body/div[3]/div[1]/h1/span[1]/text()')
print(f"电影名称：{film_name}")
mylist.append(film_name)

# 上映日期
plan_date = selector.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/span[10]/text()')
print(f"上映日期：{plan_date}")
mylist.append(plan_date)

# 评分
rating = selector.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/strong/text()')
print(f"评分：{rating}")
mylist.append(rating)

import pandas as pd

movie1 = pd.DataFrame(data=mylist)

# Mac使用utf8字符集
movie1.to_csv('./movie1.csv', encoding='gbk', index=False, header=False)
