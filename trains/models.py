# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Train(models.Model):
    train_no = models.CharField("输入车次", max_length=30)
    std_train_no = models.CharField("标准车次", max_length=50)
    start_station = models.CharField("始发站",max_length=30)
    start_time = models.TimeField("始发时间")
    end_station = models.CharField("终点站", max_length=30)
    end_time = models.TimeField("到达时间")

    def __unicode__(self):
        return self.train_no

class Station(models.Model):
    types = {0: "始发站",
             1: "中途站",
             2: "终点站"}
    name = models.CharField("站名", max_length=30)
    arrive_time = models.TimeField("到站时间")
    out_time = models.TimeField("出站时间")
    station_type  = models.IntegerField(choices=types,verbose_name='车站类型',default=1)

    def __unicode__(self):
        return self.name
