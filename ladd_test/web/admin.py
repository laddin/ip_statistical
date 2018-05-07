from django.contrib import admin
from .models import web_info


# Register your models here.
@admin.register(web_info)
class web_info_admin(admin.ModelAdmin):
    # 列表显示
    list_display = (
    "id", "web_name", "web_status", "web_data_status", "web_getstop", "web_record", "web_date", "web_update")
    ordering = ("-id",)
    # 筛选器
    date_hierarchy = "web_date"

# admin.site.register(web_info, web_info_admin)
