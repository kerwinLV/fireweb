# coding=utf-8
# @Time    : 2020/6/12 13:28
# @Author  : kerwin
# @File    : updatedata.py
import time
from tools.sqlconn import get_pool

conn = get_pool().connection()
cur = conn.cursor()
sql = "select * from anqing_xiaofang_copy1"
cur.execute(sql)

data = cur.fetchall()
for i in data:
    # print(i["t_time"])
    t_time = i["t_time"].replace("- "," ")
    print(i["t_time"])
    # print(t_time)
    # 将其转换为时间数组
    timeStruct = time.strptime(t_time, "%Y-%m-%d %H:%M")
    # 转换为时间戳:
    timeStamp = int(time.mktime(timeStruct))
    print(timeStamp)
    sql = "update anqing_xiaofang_copy1 set t_time=%s where id=%s"
    cur.execute(sql,(timeStamp,i["id"]))
    conn.commit()
# print(data)
cur.close()
conn.close()



t = "2017-11-24 17:30:00"
#将其转换为时间数组
timeStruct = time.strptime(t, "%Y-%m-%d %H:%M:%S")
#转换为时间戳:
timeStamp = int(time.mktime(timeStruct))
print(timeStamp)

