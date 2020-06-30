# coding=utf-8
# @Time    : 2020/6/12 17:25
# @Author  : kerwin
# @File    : args_tools.py
from flask import request
def get_args(args1,default):
    if args1 in request.args:
        args2 = request.args[args1]
    else:
        args2 = default

    return args2


def get_json(args1,default):
    print(request.json)
    if args1 in request.json:
        args2 = request.json.get(args1)
    else:
        args2 = default

    return args2