#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 10:04
# @File    : p6_short.py


from selenium import webdriver
import time
import os
os.putenv('PATH', 'D:\\Program Files\\Mozilla Firefox\\')

try:
    browser = webdriver.Firefox()

    browser.get("https://movie.douban.com/subject/1292052/")
    time.sleep(1)

    btm1 = browser.find_element_by_xpath('//*[@id="hot-comments"]/a')

    btm1.click()
    time.sleep(1)
    print(browser.page_source)

except Exception as e:
    print(e)