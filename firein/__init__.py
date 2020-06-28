# coding=utf-8
# @Time    : 2020/6/19 9:59
# @Author  : kerwin
# @File    : __init__.py.py
import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    # create and configure the app
    app = Flask(__name__)
    # app = db.init_app(app)

    from .data import databp
    app.register_blueprint(databp,url_prefix='/databp')
    return app