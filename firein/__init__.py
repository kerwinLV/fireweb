# coding=utf-8
# @Time    : 2020/6/19 9:59
# @Author  : kerwin
# @File    : __init__.py.py
import os

from flask import Flask
from flask_apscheduler import APScheduler
# from flask.ext.sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

def create_app():
    # create and configure the app
    app = Flask(__name__)
    # app = db.init_app(app)
    #启动定时器
    scheduler = APScheduler()

    app.config.update(
        {"SCHEDULER_API_ENABLED": True,
         "JOBS": [{"id": "1",  # 任务ID
                   "func": "firein.scheduled_tasks:aps_test",  # 任务位置
                   "trigger": "cron",  # 触发器
                   "hour":"11",
                   "minute": "20",  # 时间间隔
                   "args": ("11",)}]
         }
    )
    scheduler.init_app(app)
    scheduler.start()

    from .data import databp
    app.register_blueprint(databp,url_prefix='/databp')
    from .scheduled_tasks import taskbp
    app.register_blueprint(taskbp, url_prefix='/taskbp')
    return app