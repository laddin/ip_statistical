from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from . import service
from .models import web_info

from django.utils import timezone


# 获取近天日期



def index(request):


    return render(request, "web/index.html")


# 当天数据
def today(request):
    today_date = timezone.now().strftime("%Y-%m-%d")

    http_name = ['web1', 'web2', 'web3', 'web4', 'web1', 'web2', 'web3', 'web4', 'web1', 'web2', 'web3', 'web4', 'web1',
                 'web2', 'web3', 'web4']
    today_ip_num = [11, 22, 3, 44, 11, 22, 3, 44, 11, 22, 3, 44, 11, 22, 3, 44]
    today_spider_num = [1231, 12412, 1231, 123, 5235, 123, 52341, 124, 54, 213, 1231, 12412, 1231, 123, 5235, 123,
                        52341, 124, 54, 213]
    today_record_num = [123, 2341, 43, 36, 213, 123, 12, 312]
    today_record_sum = [1, 23, 4, 5, 6, 7, 8, 9]
    return render(request, "web/today.html", {
        'http_name': http_name,
        'today_date': today_date,
        'today_ip_num': today_ip_num,
        'today_spider_num': today_spider_num,
        'today_record_sum': today_record_sum,
        'today_record_num': today_record_num,
    })


# 历史IP
def history_ip(request):
    history_x_Seven =service.history_x_Seven()
    data = [{'name': 'web1', 'data': [11, 2, 3, 4, 55]}, {'name': 'web2', 'data': [13, 4, 5, 36, 7]},
            {'name': 'web3', 'data': [5, 6, 72, 8, 19]}]
    return render(request, "web/history_ip.html", {
        'history_x_Seven': history_x_Seven,
        'history_x_all': history_x_Seven,
        'data_Seven': data,
        'data': data

    })


# 历史爬虫
def history_spider(request):
    history_http_name = ['xq1', 'xq2', 'xq3', 'xq4']
    data = [{'name': 'web1', 'data': [11, 2, 3, 4, 55]}, {'name': 'web2', 'data': [13, 4, 5, 36, 7]},
            {'name': 'web3', 'data': [5, 6, 72, 8, 19]}]
    return render(request, "web/history_spider.html", {
        'history_x_Seven': history_http_name,
        'history_x_all': history_http_name,
        'data_Seven': data,
        'data': data
    })


# 历史目录
def history_record(request):
    history_http_name = ['xq1', 'xq2', 'xq3', 'xq4']
    data = [{'name': 'web1', 'data': [11, 2, 3, 4, 55]}, {'name': 'web2', 'data': [13, 4, 5, 36, 7]},
            {'name': 'web3', 'data': [5, 6, 72, 8, 19]}]
    return render(request, "web/history_record.html", {
        'history_x_Seven': history_http_name,
        'history_x_all': history_http_name,
        'data_Seven': data,
        'data': data
    })
