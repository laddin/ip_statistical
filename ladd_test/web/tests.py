from django.test import TestCase

import datetime

aaa = [{'web_name': '1666', 'web_ip_phone': 3242, 'web_ip_pc': 1231, 'web_baidu_spider': 123,
        'web_baidu_record': 54123, 'web_baidu_today_recory': 123},
       {'web_name': '213123', 'web_ip_phone': 1, 'web_ip_pc': 324, 'web_baidu_spider': 234,
        'web_baidu_record': 123, 'web_baidu_today_recory': 123}]
bbb = {}

for i in aaa:
    for a in i.keys():
        if a in bbb.keys():
            bbb[a].append(i[a])
        else:
            bbb[a]=[i[a]]

a = [1,23,4,5]
b = [4,2,1,5]

v = list(map(lambda x: x[0]+x[1], zip(a, b)))
print(v)