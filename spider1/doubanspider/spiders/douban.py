import scrapy
from bs4 import BeautifulSoup as bfs
import sys

sys.path.append("D:\\user\\pys\\geekbangtrain\\")
print("current path:")
print(sys.path)
from spider1.doubanspider.items import DoubanspiderItem


class DoubanSpider(scrapy.Spider):
    # 爬虫名称和访问域名（只能在这个域名下进行爬虫）
    name = 'douban'
    allowed_domains = ['movie.douban.com']

    # 起始url列表
    start_urls = ['https://movie.douban.com/top250']

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        for i in range(0, 10):
            url = f'{self.start_urls[0]}?start={i * 25}'
            # yield scrapy.Request(url=url, callback=self.parse)
            yield scrapy.Request(url=url, callback=self.parse2)
            # url 请求访问的网址
            # callback 回调函数，引擎会将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数，callback回调函数会调用
    def parse(self, response):
        items = []
        soup = bfs(response.text, 'html.parser')
        title_list = soup.find_all('div', attrs={'class': 'hd'})
        for i in title_list:
            # 在items.py定义
            item = DoubanspiderItem()
            title = i.find('a').find('span').text
            link = i.find('a'.find('href'))
            item['title'] = title
            item['link'] = link
            items.append(item)
        return items

    # 解析函数，callback回调函数会调用
    def parse2(self, response):
        soup = bfs(response.text, 'html.parser')
        title_list = soup.find_all('div', attrs={'class': 'hd'})
        for i in title_list:
            # 在items.py定义
            item = DoubanspiderItem()
            title = i.find('a').find('span').text
            link = i.find('a'.find('href'))
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(url=link,meta={'item':item},callback=self.parse3)

    # 解析具体页面
    def parse3(self,response):
        item = response.meta['item']
        soup = bfs.
