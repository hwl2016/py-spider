# encoding=utf-8
import json
from datetime import date, datetime, timedelta, time

import pymysql

#连接配置信息
config = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'123456',
    'db':'demo',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor,
}
# 创建连接
connection = pymysql.connect(**config)

def query():
    # 执行sql语句
    try:
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            sql = 'SELECT id, name, age, sex FROM student'
            cursor.execute(sql)
            # 获取查询结果
            result = cursor.fetchall()
            print(json.dumps(result, indent=4))
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close()

def add():
    # 获取明天的时间
    tomorrow = datetime.now().date() + timedelta(days=1)
    # 执行sql语句
    try:
        with connection.cursor() as cursor:
            # 执行sql语句，插入记录
            sql = 'INSERT INTO student (name, age, sex, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)'
            cursor.execute(sql, ('Robin', 20, 11, datetime.now(), datetime.now()))
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close()

if __name__ == '__main__':
    add()