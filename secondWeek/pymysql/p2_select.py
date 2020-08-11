#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 23:39
# @File    : p2_select.py


import pymysql


class DbConnectionError(Exception):
    """先当固定的用法记着"""

    def __init__(self, info):
        super(DbConnectionError, self).__init__(info)
        self._info = info

    def __str__(self):
        return self._info


db_info = {
    'host': '192.168.102.160',
    'port': 3306,
    'user': 'root',
    'password': 'Cole+123',
    'db': 'pythontest',
    'charset': 'utf8mb4'
}

# 建立连接
try:
    connection = pymysql.connect(host=db_info['host'],
                                 port=db_info['port'],
                                 user=db_info['user'],
                                 password=db_info['password'],
                                 db=db_info['db'],
                                 charset=db_info['charset'])
except DbConnectionError as e:
    print(e)

try:
    with connection.cursor() as cursor:
        sql = "insert into `users` (`email`,`password`) values (%s,%s)"
        cursor.execute(sql, ('123@python.org', 'very123'))

    # connection is not autocommit by default. So you must commit to save your changes.
    connection.commit()

    with connection.cursor() as cursor:
        sql = "select `id`,`password` from `users` where `email`=%s"
        result = cursor.execute(sql, ("123@python.org"))
        print(result)
        print(cursor.fetchone())
finally:
    connection.close()
