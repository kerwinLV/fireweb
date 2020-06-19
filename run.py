# coding=utf-8
# @Time    : 2020/6/19 13:47
# @Author  : kerwin
# @File    : run.py
import os,sys
path1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path1)

from firein import create_app


if __name__=="__main__":
    app = create_app()
    app.run()
