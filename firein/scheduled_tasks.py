# coding=utf-8
# @Time    : 2020/6/29 10:18
# @Author  : kerwin
# @File    : scheduled_tasks.py
import datetime

from flask import Blueprint,current_app,jsonify

from tools.removetasks import remove_tasks
from tools.seleniumanqing import main
# scheduler = BlockingScheduler()

taskbp = Blueprint("scheduled_tasks", __name__)
now = datetime.datetime.now()
zeroToday = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                         microseconds=now.microsecond)

# 删除所有定时任务
@taskbp.route('/stop_scheduled_tasks', methods=('GET',))
def stop_scheduled_tasks():
    joblist = current_app.apscheduler.get_jobs()
    print(joblist)
    remove_tasks(joblist)
    print(current_app.apscheduler.get_jobs(), "3212312312")
    data1 = {
        "code": "200",
        "msg": "success",
        "data": ""
    }
    return jsonify(data1)


# 修改获取案情数据频率
@taskbp.route('/start_scheduled_tasks', methods=('GET',))
def start_scheduled_tasks():
    joblist = current_app.apscheduler.get_jobs()
    print(joblist)
    remove_tasks(joblist)
    current_app.apscheduler.add_job(func=main, args=("1",), trigger='cron', hour='23',minute='59', id='1')
    current_app.apscheduler.add_job(func=main, args=("2",), trigger='interval', days=2,start_date=zeroToday, id='2')
    # print(current_app.apscheduler.get_jobs())
    data1 = {
        "code": "200",
        "msg": "success",
        "data": ""
    }
    return jsonify(data1)


# def aps_test(x):
#     print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)
