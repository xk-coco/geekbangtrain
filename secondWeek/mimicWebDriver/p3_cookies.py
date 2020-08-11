#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 7:19
# @File    : p3_cookies.py


import requests

s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
s.cookies
r=s.get("http://httpbin.org/cookies")

print(r.text)

# 会话可以使用上下文管理器
with requests.Session() as s:
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')