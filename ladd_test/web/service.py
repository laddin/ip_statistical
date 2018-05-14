from .models import web_info
import datetime


# 获取时间
def history_x_Seven(num):
    QuerySet_list = list(web_info.objects.values('web_date').distinct())
    datetime_list = []
    time_list = []
    for i in QuerySet_list:
        datetime_list.append(i['web_date'])
    datetime_list.sort()
    for i in datetime_list:
        time_list.append(str(i))

    if len(time_list) < num:
        return time_list
    else:
        return time_list[-num:]


# 获取当天数据 传当天时间
def get_today_data(today_time):
    data_list = list(web_info.objects.filter(web_date=today_time).values('web_name', 'web_ip_phone',
                                                                         'web_ip_pc', 'web_baidu_spider',
                                                                         'web_baidu_record', 'web_baidu_today_recory'
                                                                         ))
    #data_list = [{'web_name': '1666', 'web_ip_phone': 3242, 'web_ip_pc': 1231, 'web_baidu_spider': 123,
    #              'web_baidu_record': 54123, 'web_baidu_today_recory': 123},
    #             {'web_name': '213123', 'web_ip_phone': 1, 'web_ip_pc': 324, 'web_baidu_spider': 234,
    #              'web_baidu_record': 123, 'web_baidu_today_recory': 123}]

    today_data_info = {}
    for i in data_list:
        for a in i.keys():
            if a in today_data_info.keys():
                today_data_info[a].append(i[a])
            else:
                today_data_info[a] = [i[a]]

    return today_data_info

    # 获取历史IP 传时间段


def get_history_ip(his_time):
    # his_time = ["2018-05-07", "2018-05-13"]

    # aaa = list(web_info.objects.filter(web_date__range=his_time).values('web_name', 'web_ip_phone', 'web_ip_pc'))
    # for i in aaa:
    pass


# 获取历史爬虫
def get_history_spider(his_time):
    pass


# 获取历史目录
def get_history_record(his_time):
    pass
