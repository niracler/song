from __future__ import absolute_import, unicode_literals
from celery import shared_task
import datetime

@shared_task
def add(x, y):
    res = x + y
    time_format = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('当前时间为：' + time_format + ' ,两个数相加的结果为：')
    print(res)
    return res

@shared_task
def mul(x, y):
    res = x * y
    time_format = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('当前时间为：' + time_format + ' ,两个数相乘的结果为：')
    print(res)
    return res

@shared_task
def xsum(numbers):
    res = sum(numbers)
    print(res)
    return res