from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from . import service
from .models import web_info


from django.utils import timezone


# 获取近天日期



def index(request):
    #aaa = web_info.objects.filter(web_date="2018-05-13")
    #aaa = web_info.objects.filter(web_date__range=["2018-05-07","2018-05-13"]).values('web_name','web_ip_phone','web_ip_pc')
    aaa = list(web_info.objects.filter(web_date="2018-05-07").values('web_name', 'web_ip_phone',
                                                                         'web_ip_pc', 'web_baidu_spider',
                                                                         'web_baidu_record', 'web_baidu_today_recory'
                                                                         ))
    #print(aaa,type(aaa))

    return render(request, "web/index.html")


# 当天数据
def today(request):
    today_date = service.history_x_Seven(1)
    #print(today_date,type(today_date))
    today_data_info = service.get_today_data(today_date[0])
    http_name = today_data_info['web_name']
    ip_pc = today_data_info['web_ip_pc']
    ip_phone = today_data_info['web_ip_phone']
    today_ip_num = list(map(lambda x: x[0]+x[1], zip(ip_pc, ip_phone)))
    today_spider_num = today_data_info['web_baidu_spider']
    today_record_num = today_data_info['web_baidu_today_recory']
    today_record_sum = today_data_info['web_baidu_record']
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
    history_x_Seven =service.history_x_Seven(7)
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
