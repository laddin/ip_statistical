from django.urls import path
from . import views

urlpatterns = [
    path('<int:web_id>', views.web_detail, name="web_detail"),
    path('', views.index),
    path('index.html', views.index),
    path('today.html', views.today),
    path('history.html', views.history),
    path('today_ip.html', views.today_ip),
]
