from .models import web_info
import datetime


def history_x_Seven():
    QuerySet_list = list(web_info.objects.values('web_date').distinct())
    datetime_list = []
    x_Seven = []
    for i in QuerySet_list:
        datetime_list.append(i['web_date'])
    datetime_list.sort()
    for i in datetime_list:
        x_Seven.append(str(i))
    if len(x_Seven) < 7:

        return x_Seven
    else:
        return x_Seven[-7:]
