import scrapy


# export http_proxy='http://52.179.231.206:80' -- mac和linux
# setting 增加 scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware
# 通过 Request.meta['proxy'] 读取 http_proxy 环境变量加载代理
# import os
# os.putenv('http_proxy', 'http://52.179.231.206:80')

class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    # 功能：通过ip查看请求的ip地址
    start_urls = ['http://httpbin.org/ip']

    # 功能：通过headers查看user-agent
    # start_urls = ['http://httpbin.org/headers']

    def parse(self, response):
        print(response.text)
