#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 7:37
# @File    : p5_cockie_webdriver.py


from selenium import webdriver
import time
import os

# print(os.environ['PATH'])
# os.environ['PATH'] = os.environ['PATH'] + ";D:\\Program Files\\Mozilla Firefox\\"
# print(os.environ['PATH'])

os.putenv('PATH', 'D:\\Program Files\\Mozilla Firefox\\')
# putenv() 的调用不会更新 os.environ，因此最好使用 os.environ 对变量赋值。
# print(os.getenv('PATH'))

try:
    # 需要安装Firefox driver，和浏览器版本保持一致，地址：
    #  	https://github.com/mozilla/geckodriver/releases
    brower = webdriver.Firefox()
    brower.get("https://www.douban.com/")
    time.sleep(1)
    brower.switch_to.frame(brower.find_elements_by_tag_name('iframe')[0])
    btm1 = brower.find_element_by_xpath('//ul[@class="tab-start"]/li[2]')
    btm1.click()

    brower.find_element_by_xpath('//*[@id="username"]').send_keys('xk1990coco@163.com')
    brower.find_element_by_id('password').send_keys('DBXXxk19990@')
    time.sleep(1)
    brower.find_element_by_xpath('//a[contains(@class,"btn btn-account")]').click()

    cookies_value = brower.get_cookies()  # 获取cookie值
    print(cookies_value)

    time.sleep(3)


except Exception as e:
    print(e)
finally:
    brower.close()
