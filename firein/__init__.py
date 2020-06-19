# coding=utf-8
# @Time    : 2020/6/19 9:59
# @Author  : kerwin
# @File    : __init__.py.py
import os

from flask import Flask

def create_app():
    # create and configure the app
    app = Flask(__name__)

    from .data import databp
    app.register_blueprint(databp,url_prefix='/databp')
    return app