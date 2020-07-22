#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 7:51
# @File    : 1a_requests.py

import requests
from bs4 import BeautifulSoup as bs


def get_movie_name(db_url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
    header = {'user-agent': user_agent}
    response = requests.get(db_url, headers=header)  # headers参数是为了尽量模拟浏览器的功能
    print(f"返回码：{response.status_code}")
    bs_info = bs(response.text, 'html.parser')
    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        # print(f"过滤出来的标签：{tags}")
        for atag in tags.find_all('a'):
            # print(f"a标签的值：{atag}")
            print(f"电影名称：{atag.find('span').text}")
            print(f"电影链接：{atag.get('href')}")


# 生成包含所有页面的元组
db_urls = tuple(f"https://movie.douban.com/top250?start={page * 25}&filter=" for page in range(10))
for numb in range(1, len(db_urls) + 1):
    print(f"页面{numb}:{db_urls[numb - 1]}")

# 控制请求频率，引入time
from time import sleep

sleep(10)

for page in db_urls:
    get_movie_name(page)
