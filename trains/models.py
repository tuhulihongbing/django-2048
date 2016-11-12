# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Train(models.Model):
    train_no = models.CharField("车次", max_length=50)
    stations = models.ManyToManyField('Station', through='Membership')

    def __unicode__(self):
        return self.train_no

class Station(models.Model):
    name = models.CharField("站名", max_length=30)

    def __unicode__(self):
        return self.name

class Membership(models.Model):
    types = {0: "始发站",
             1: "中途站",
             2: "终点站"}
    train = models.ForeignKey(Train , verbose_name='车次')
    station = models.ForeignKey(Station, verbose_name="站名")
    arrive_time = models.TimeField("到站时间")
    out_time = models.TimeField("发车时间")
    sequences = models.IntegerField("发车顺序")
    station_type = models.IntegerField(choices=types, verbose_name='车站类型', default=1)

    def __unicode__(self):
        return self.station_type