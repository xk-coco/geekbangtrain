#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 7:51
# @File    : 1a_requests.py

import requests

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
header = {'user-agent': user_agent}

doubanurl = "https://movie.douban.com/top250?start=0"

response = requests.get(doubanurl, headers=header)  # headers参数是为了尽量模拟浏览器的功能

response = requests.get(doubanurl) # return 418

print(response.text)
print(f"返回码：{response.status_code}")
