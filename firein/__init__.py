# coding=utf-8
# @Time    : 2020/6/19 9:59
# @Author  : kerwin
# @File    : __init__.py.py
import os
import datetime
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
    # from test.test5 import get_joblist
    now = datetime.datetime.now()
    zeroToday = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                         microseconds=now.microsecond)

    # app.config.update(
    #     {"SCHEDULER_API_ENABLED": True,
    #      "JOBS": [{"id": "1",  # 任务ID
    #                "func": "firein.scheduled_tasks:aps_test",  # 任务位置
    #                "trigger": "cron",  # 触发器
    #                "hour": "14",
    #                "minute": "08",  # 时间间隔
    #                "args": ("1",)}
    #               ]
    #      }
    # )
    # app.config.update(
    #     {"SCHEDULER_API_ENABLED": True,
    #      "JOBS": get_joblist()
    #      }
    # )
    app.config.update(
        {"SCHEDULER_API_ENABLED": True,
         "JOBS": [{"id": "1",  # 任务ID
                   "func": "tools.seleniumanqing:main",  # 任务位置
                   "trigger": "cron",  # 触发器
                   "hour":"23",
                   "minute": "59",  # 时间间隔
                   "args": ("1",)},
                  {"id": "2",  # 任务ID
                   "func": "tools.seleniumanqing:main",  # 任务位置
                   "trigger": "interval",  # 触发器
                   "days": 2,
                   "start_date":zeroToday,  # 时间间隔
                   "args": ("2",)}
                  ]
         }
    )
    scheduler.init_app(app)
    scheduler.start()

    from .data import databp
    app.register_blueprint(databp,url_prefix='/databp/v1')
    from .scheduled_tasks import taskbp
    app.register_blueprint(taskbp, url_prefix='/taskbp/v1')
    return app