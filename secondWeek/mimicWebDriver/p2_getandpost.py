#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 6:54
# @File    : p2_getandpost.py


import requests

# http 协议的get方法
r = requests.get('https://github.com')
r.status_code
r.headers['content-type']

# r.json()

# http 协议的post方法
r = requests.post('http://httpbin.org/post', data={'key': 'value'})
r.json()
