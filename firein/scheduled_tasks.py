# coding=utf-8
# @Time    : 2020/6/29 10:18
# @Author  : kerwin
# @File    : scheduled_tasks.py

from flask import Blueprint
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
from flask import current_app
# scheduler = BlockingScheduler()

taskbp = Blueprint("scheduled_tasks",__name__)

@taskbp.route('/stop_scheduled_tasks',methods=('GET',))
def stop_scheduled_tasks():
    print(current_app.apscheduler.get_jobs())
    current_app.apscheduler.remove_job("1")
    print(current_app.apscheduler.get_jobs(),"3212312312")
    print("remove")
    return "remove"


@taskbp.route('/start_scheduled_tasks',methods=('GET',))
def start_scheduled_tasks():
    def aps_test(x):
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)
    current_app.apscheduler.add_job(func=aps_test, args=("定时任务",), trigger='cron', second='*/5', id='1')
    print(current_app.apscheduler.get_jobs())
    return "ok"


def aps_test(x):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)