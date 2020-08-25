#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 0:01
# @File    : miniScrapy.py

import requests
from lxml import etree
from queue import Queue
import threading
import json

FLAG = False  # 全局控制变量


class CrawlThread(threading.Thread):
    """
    爬虫类
    """

    def __init__(self, thread_id, queue: Queue, dataqueue: Queue):
        super(CrawlThread, self).__init__()
        self.thread_id = thread_id
        self.queue = queue
        self.dataqueue = dataqueue

    def run(self) -> None:
        """
        重写run方法
        :return: None
        """
        print(f"crawl线程:{self.thread_id}启动")
        self.scheduler()
        print(f"crawl线程:{self.thread_id}结束")

    # 模拟任务调度
    def scheduler(self):
        while True:
            if self.queue.empty():  # 队列为空不处理
                break
            else:
                page = self.queue.get()
                print(f"下载线程:{self.thread_id}，下载页面:{page + 1}")
                url = f"https://book.douban.com/top250?start={page * 25}"
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'
                }
                try:
                    # downloader下载器
                    response = requests.get(url, headers=headers)
                    self.dataqueue.put(response.text)
                except Exception as e:
                    print(f"下载出现异常：{e}")


class ParserThread(threading.Thread):
    """
    页面解析类
    """

    def __init__(self, thread_id, queue: Queue, file):
        threading.Thread.__init__(self)  # 上面使用了super()
        self.thread_id = thread_id
        self.queue = queue
        self.file = file

    def run(self) -> None:
        print(f"parse线程：{self.thread_id}启动")
        # print(f"FLAG值:{FLAG}")
        while not FLAG:
            try:
                item = self.queue.get(block=False)  # 使用False参数，当队列为空，抛出异常
                # print(f"item:{item}")
                if not item:  # 为什么要判断？
                    continue
                self.parse_data(item)
                self.queue.task_done()  # GET之后检测是否会阻塞
            except Exception as e:
                # print(f"parse run error:{e}")
                pass
        print(f"parse线程：{self.thread_id}结束")

    def parse_data(self, item):
        """
        解析网页内容的函数
        :param item:
        :return:
        """
        try:
            html = etree.HTML(item)
            books = html.xpath('//div[@class="pl2"]')
            for book in books:
                try:
                    title = book.xpath('./a/text()')[0]
                    link = book.xpath('./a/@href')[0]
                    response = {
                        'title': title,
                        'link': link
                    }

                    # print(f"response解析数据:{response}")

                    # 解析方法和scrapy相同，再构造一个json
                    json.dump(response, fp=self.file, ensure_ascii=False)
                except Exception as e:
                    print(f"book error:{e}")
        except Exception as e:
            print(f"page error:{e}")


if __name__ == '__main__':
    dataqueue = Queue()
    try:
        # 将结果保存到json文件中
        output = open('book.json', 'w+', encoding='utf-8')

        # 任务队列，存放网页
        pageQueue = Queue(20)
        for page in range(0, 11):
            pageQueue.put(page)

        # 爬虫线程
        crawl_threads = []
        crawl_name_list = ['crawl_1', 'crawl_2', 'crawl_3']
        for thread_id in crawl_name_list:
            thread = CrawlThread(thread_id, pageQueue, dataqueue)
            thread.start()
            crawl_threads.append(thread)

        # 解析线程
        parse_thread = []
        parse_name_list = ['parse_1', 'parse_2', 'parse_3']
        for thread_id in parse_name_list:
            thread = ParserThread(thread_id, dataqueue, output)
            thread.start()
            parse_thread.append(thread)

        # 结束crawl线程
        for t in crawl_threads:
            t.join()

        # 结束parse线程
        FLAG = True
        for t in parse_thread:
            t.join()
    except Exception as e:
        pass
    finally:
        output.close()
        print(f"退出主线程")
