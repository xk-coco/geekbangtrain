#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 12:25
# @File    : ocrVerification.py


import requests
import os
from PIL import Image
import pytesseract

# 下载图片
# session = requests.session()
# img_url = "http://www.pythonchallenge.com/pc/def/ocr.jpg"
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
# headers = {'user-agent': user_agent}
#
# r = session.get(img_url, headers=headers)
# with open('ocr.jpg','wb') as f:
#     f.write(r.content)

# 打开并显示文件
# im = Image.open(r'D:\user\pys\geekbangtrain\testDatafile\python_logo.jpg')
im = Image.open('ocr.jpg')
# im.show()

# 灰度图片
gray = im.convert('L')
gray.save('ocr_gray.jpg')
im.close()

# 二值化
threshold = 100
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

out = gray.point(table, '1')
out.save('ocr_th.jpg')

th = Image.open('ocr_th.jpg')
print(pytesseract.image_to_string(th, lang='chi_sim+eng'))
