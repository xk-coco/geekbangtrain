#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 7:42
# @File    : p1_pymysql.py

# 推荐使用PyMySQL模块
# 一般流程:
#   开始-创建connection-获取cursor-CRUD(查询并获取数据)-关闭cursor-关闭connection-结束


import pymysql

db_info = {
    'host': '192.168.102.160',
    'port': 3306,
    'user': 'root',
    'password': 'Cole+123',
    'db': 'pythontest'
}

sqls = ['select 1', 'select VERSION()']

result = []


class ConnDB(object):
    def __init__(self, dbinfo: dir, sql_express: list):
        self.host = dbinfo['host']
        self.port = dbinfo['port']
        self.user = dbinfo['user']
        self.password = dbinfo['password']
        self.db = dbinfo['db']
        self.sql_express = sql_express

    def run(self):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )
        # 建立游标的时候就是开启了一个隐形的事务
        cur = conn.cursor()
        try:
            for command in self.sql_express:
                cur.execute(command)
                result.append(cur.fetchmany())
            # 关闭游标
            cur.close()
            conn.commit()
        except:
            # 有异常则会回滚，commit和rollback是在conn对象上
            conn.rollback()
        # 关闭数据库连接
        conn.close()


if __name__ == '__main__':
    conn = ConnDB(db_info,sqls)
    conn.run()
    print(result)
