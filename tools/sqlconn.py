# coding=utf-8
# @Time    : 2020/6/12 10:55
# @Author  : kerwin
# @File    : sqlconn.py
import pymysql
from DBUtils.PooledDB import PooledDB


pool = PooledDB(pymysql, 10,
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='fire',
                charset='utf8',
cursorclass = pymysql.cursors.DictCursor
)

