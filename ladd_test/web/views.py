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
    data = "当日数据 主页"
    return render(request, "web/today.html", {'data': data})


def history(request):
    return render(request, "web/history.html")


def today_ip(request):
    data = "today_ip 主页"
    return render(request, "web/today_ip.html", {'data': data})
