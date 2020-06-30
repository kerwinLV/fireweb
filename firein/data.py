# coding=utf-8
# @Time    : 2020/6/19 13:41
# @Author  : kerwin
# @File    : data.py

from flask import Blueprint,jsonify
from flask import current_app

from tools.sqlconn import get_pool
from tools.args_tools import get_args,get_json
from tools.localcgstamp import localcgst
from .scheduled_tasks import start_scheduled_tasks

pool = get_pool()
databp = Blueprint('data',__name__)

# 获取案情数据接口 参数page size start_time end_time
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
        cur.execute(sql, (start_time,end_time,(int(page) - 1) * int(size), int(size)))
        data = cur.fetchall()
        sql = "select count(1) as co from anqing_xiaofang_a where release_time between %s and %s order by release_time desc"
        cur.execute(sql, (start_time, end_time,))
        count1 = cur.fetchone()["co"]
        # count1 = len(data)
    else:
        sql = "select * from anqing_xiaofang_a order by release_time desc limit %s,%s"
        cur.execute(sql, ((int(page) - 1) * int(size), int(size)))
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

#获取案情来源数据接口 参数page  size
@databp.route('/get_sourcefrom',methods = ('GET',))
def get_sourcefrom():
    page = get_args("page", 1)
    size = get_args("size", 14)
    conn = pool.connection()
    cur = conn.cursor()
    sql = "SELECT sourcefrom.id,nickname,url,type,timeset from sourcefrom INNER JOIN timeset ON sourcefrom.timesetid=timeset.id limit %s,%s"
    cur.execute(sql ,((int(page) - 1) * int(size), int(size)))
    data = cur.fetchall()
    sql = "SELECT count(1) as co from sourcefrom INNER JOIN timeset ON sourcefrom.timesetid=timeset.id"
    cur.execute(sql)
    count1 = cur.fetchone()["co"]
    cur.close()
    conn.close()
    data1 = {
        "code": "200",
        "msg": "success",
        "total": count1,
        "data": data
    }
    return jsonify(data1)


#获取频率接口
@databp.route('/get_timeset',methods = ('GET',))
def get_timeset():
    conn = pool.connection()
    cur = conn.cursor()
    sql = "SELECT * from timeset"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    data1 = {
        "code": "200",
        "msg": "success",
        "data": data
    }
    return jsonify(data1)

#修改数据来源频率接口 参数sourcefrom_id  timeset_id
@databp.route('/post_modify_sourcefrom',methods = ('POST',))
def post_modify_sourcefrom():
    sourcefrom_id = get_json("sourcefrom_id","")
    timeset_id = get_json("timeset_id","")
    print(id)
    if not sourcefrom_id or not timeset_id:
        data1 = {
            "code": "00000002",
            "msg": "缺少参数",
            "data": ""
        }
        return jsonify(data1)
    conn = pool.connection()
    cur = conn.cursor()
    sql = "update sourcefrom set timesetid=%s where id=%s"
    cur.execute(sql,(timeset_id,sourcefrom_id))
    conn.commit()
    cur.close()
    conn.close()
    start_scheduled_tasks()
    joblist = current_app.apscheduler.get_jobs()
    print(joblist)
    data1 = {
        "code": "200",
        "msg": "success",
        "data": ""
    }
    return jsonify(data1)



#返回数据来源关键字 参数sourcefrom_id  timeset_id
@databp.route('/get_keyword',methods = ('GET',))
def get_keyword():
    conn = pool.connection()
    cur = conn.cursor()
    sql = "select * from keyword"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    data1 = {
        "code": "200",
        "msg": "success",
        "data": data
    }
    return jsonify(data1)


#修改数据来源关键字 参数 id  keyword
@databp.route('/post_modify_keyword',methods=('POST',))
def post_modify_keyword():
    id = get_json("id", "")
    keyword = get_json("keyword", "")
    print(id)
    if not id or not keyword:
        data1 = {
            "code": "00000002",
            "msg": "缺少参数",
            "data": ""
        }
        return jsonify(data1)
    conn = pool.connection()
    cur = conn.cursor()
    sql = "select * from keyword where keyword=%s"
    cur.execute(sql, (keyword))
    data = cur.fetchone()
    if data:
        data1 = {
            "code": "00000002",
            "msg": "关键字已存在",
            "data": ""
        }
        return jsonify(data1)
    sql = "update keyword set keyword=%s where id=%s"
    cur.execute(sql,(keyword,id))
    conn.commit()
    cur.close()
    conn.close()
    data1 = {
        "code": "200",
        "msg": "success",
        "data": ""
    }
    return jsonify(data1)


#添加数据来源关键字 参数  keyword
@databp.route('/post_add_keyword',methods = ('POST',))
def post_add_keyword():
    keyword = get_json("keyword", "")
    # print(id)
    if not keyword:
        data1 = {
            "code": "00000002",
            "msg": "缺少参数",
            "data": ""
        }
        return jsonify(data1)
    conn = pool.connection()
    cur = conn.cursor()
    sql = "select * from keyword where keyword=%s"
    cur.execute(sql, (keyword))
    data = cur.fetchone()
    if data:
        data1 = {
            "code": "00000002",
            "msg": "关键字已存在",
            "data": ""
        }
        return jsonify(data1)
    sql = "insert into keyword (keyword) values (%s)"
    cur.execute(sql,(keyword))
    conn.commit()
    cur.close()
    conn.close()
    data1 = {
        "code": "200",
        "msg": "success",
        "data": ""
    }
    return jsonify(data1)

