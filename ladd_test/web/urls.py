from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index.html', views.index),
    path('today.html', views.today),
    path('history_ip.html', views.history_ip),
    path('history_spider.html', views.history_spider),
    path('history_record.html', views.history_record),
]
