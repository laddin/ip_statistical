from django.db import models


class web_info(models.Model):
    web_date = models.DateField(auto_now_add=True, verbose_name="日期")
    web_name = models.CharField(max_length=100, verbose_name="网站名称")
    web_ip_phone = models.IntegerField(verbose_name="手机ip")
    web_ip_pc = models.IntegerField(verbose_name="pc_ip")
    web_baidu_spider = models.IntegerField(verbose_name="百度爬虫")
    web_baidu_record = models.IntegerField(verbose_name="百度收录")
    web_baidu_today_recory = models.IntegerField(verbose_name="百度当天收录")
    web_status = models.BooleanField(default=True, verbose_name="网站状态")
    web_record = models.BooleanField(default=True, verbose_name="备案")
    web_getstop = models.BooleanField(default=True, verbose_name="长城防火墙")
    web_data_status = models.BooleanField(default=True, verbose_name="目录状态")
