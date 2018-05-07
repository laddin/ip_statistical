from django.urls import path
from . import views

urlpatterns = [
    path('<int:web_id>', views.web_detail, name="web_detail"),
    path('', views.test)
]
