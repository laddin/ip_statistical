from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from .models import web_info


# Create your views here.

def web_detail(request, web_id):
    web = get_object_or_404(web_info, pk=web_id)
    return HttpResponse(web.web_name)


def index(request):
    # aaa = web_info.objects.all()
    return render(request, "web/index.html")

def today(request):
    today_date = timezone.now().strftime("%Y-%m-%d")
    # print(today_date,type(today_date))
    http_name = ['web1', 'web2', 'web3', 'web4', 'web1', 'web2', 'web3', 'web4', 'web1', 'web2', 'web3', 'web4', 'web1',
                 'web2', 'web3', 'web4']
    today_ip_num = [11, 22, 3, 44, 11, 22, 3, 44, 11, 22, 3, 44, 11, 22, 3, 44]
    today_spider_num = [1231, 12412, 1231, 123, 5235, 123, 52341, 124, 54, 213, 1231, 12412, 1231, 123, 5235, 123,
                        52341, 124, 54, 213]
    today_record_num = [123, 2341, 43, 36, 213, 123, 12, 312]
    return render(request, "web/today.html", {'http_name': http_name,
                                              'today_date': today_date,
                                              'today_ip_num': today_ip_num,
                                              'today_spider_num': today_spider_num,
                                              'today_record_num': today_record_num,
                                              })


def history(request):
    return render(request, "web/history.html")


def today_ip(request):
    data = "today_ip 主页"
    return render(request, "web/today_ip.html", {'data': data})
