# coding=utf-8
# @Time    : 2020/6/12 17:37
# @Author  : kerwin
# @File    : localcgstamp.py
import time
def localcgst(locatime):
    try:
        timeStruct = time.strptime(locatime, "%Y-%m-%d %H:%M:%S")
            # 转换为时间戳:
        timeStamp = int(time.mktime(timeStruct))
    except Exception as e:
        return e
    return timeStamp


def localcgst2(locatime):
    try:
        timeStruct = time.strptime(locatime, "%Y-%m-%d")
            # 转换为时间戳:
        timeStamp = int(time.mktime(timeStruct))
    except Exception as e:
        return e
    return timeStamp


def localcgst3(locatime):
    try:
        timeStruct = time.strptime(locatime, "%Y-%m-%d %H:%M")
            # 转换为时间戳:
        timeStamp = int(time.mktime(timeStruct))
    except Exception as e:
        return e
    return timeStamp