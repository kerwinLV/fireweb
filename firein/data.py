# coding=utf-8
# @Time    : 2020/6/19 13:41
# @Author  : kerwin
# @File    : data.py

from flask import Blueprint,jsonify

from tools.sqlconn import get_pool
from tools.args_tools import get_args
from tools.localcgstamp import localcgst

pool = get_pool()
databp = Blueprint('data',__name__)

@databp.route('/get_fire_date', methods=('GET',))
def get_date():
    page = get_args("page",1)
    size = get_args("size",7)
    start_time =get_args("start_time","")
    end_time = get_args("end_time","")
    conn = pool.connection()
    cur = conn.cursor()
    # request.json.get("page")
    if start_time and end_time:
        start_time = int(localcgst(start_time))
        end_time = int(localcgst(end_time))
        print(start_time,end_time)
        if start_time > end_time:
            data1 = {
                "code": "00000002",
                "msg": "时间参数错误",
                "data": [],
            }
            return jsonify(data1)
        sql = "select * from anqing_xiaofang_a where release_time between %s and %s order by release_time desc limit %s,%s"
        cur.execute(sql, (start_time,end_time,(int(page) - 1) * 7, int(size)))
        data = cur.fetchall()
        sql = "select count(1) as co from anqing_xiaofang_a where release_time between %s and %s order by release_time desc"
        cur.execute(sql, (start_time, end_time,))
        count1 = cur.fetchone()["co"]
        # count1 = len(data)
    else:
        sql = "select * from anqing_xiaofang_a order by release_time desc limit %s,%s"
        cur.execute(sql, ((int(page) - 1) * 7, int(size)))
        data = cur.fetchall()
        sql = "select count(1) as co from anqing_xiaofang_a"
        cur.execute(sql)
        count1 = cur.fetchone()["co"]
    # cur.execute(sql,((int(page)-1)*7,int(size)))

    # sql = "select * from anqing_xiaofang_copy1"
    # count1 = cur.execute(sql)
    data1 = {
        "code":"200",
        "msg":"success",
        "total":count1,
        "data":data
    }
    cur.close()
    conn.close()
    return jsonify(data1)