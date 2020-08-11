#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 23:26
# @File    : p4_cookie_requests.py


import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
    'User-Agent': ua.random,
    'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony'
}

s = requests.Session()
# 会话对象：在同一个Session实例发出的所有请求之间保持cookie
# 期间使用 urllib3 的connection pooling 功能
# 向同一主机发送多个请求，底层的TCP连接会被重用，从而带来显著的性能提升。
login_url = 'https://accounts.douban.com/j/mobile/login/basic'
from_data = {
    'ck': '',
    'name': 'xk1990coco@163.com',
    'password': 'DBXXxk1990@',
    'remember': 'false',
    'ticket': ''
}

# post数据前先获取cookie
pre_login = 'https://accounts.douban.com/passport/login'
pre_resp = s.get(pre_login, headers=headers)

response = s.post(login_url, data=from_data, headers=headers)

print(response.text)
