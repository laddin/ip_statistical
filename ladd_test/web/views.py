from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from .models import web_info


# Create your views here.

def web_detail(request, web_id):
    web = get_object_or_404(web_info, pk=web_id)

    return HttpResponse(web.web_name)
