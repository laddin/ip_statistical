from django.db import models


# class domain_name(models.Model):
#    name = models.CharField(max_length=100, verbose_name="网站名称")
#    alias_name = models.CharField(max_length=100, verbose_name="网站域名")

class web_info(models.Model):
    # name = ()
    # web_name = models.IntegerField(choices=name, default=1, verbose_name="网站名称")
    web_name = models.CharField(max_length=100, verbose_name="网站名称")
    web_ip_phone = models.IntegerField(default=0, verbose_name="手机ip")
    web_ip_pc = models.IntegerField(default=0, verbose_name="pc_ip")
    web_baidu_spider = models.IntegerField(verbose_name="百度爬虫")
    web_baidu_record = models.IntegerField(verbose_name="百度收录")
    web_baidu_today_recory = models.IntegerField(default=0, verbose_name="百度当天收录")
    web_status = models.BooleanField(default=True, verbose_name="网站状态")
    web_record = models.BooleanField(default=True, verbose_name="备案")
    web_getstop = models.BooleanField(default=True, verbose_name="长城防火墙")
    web_data_status = models.BooleanField(default=True, verbose_name="目录状态")
    web_date = models.DateField(verbose_name="日期")
    web_update = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    def __str__(self):
        return "{}".format(self.web_name)
