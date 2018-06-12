# coding:utf-8
from django.db import models


class WxType(models.Model):
    # 报修类型.动态添加

    type_name = models.CharField(
        '维修类型',
        max_length=30
    )

    type_desc = models.CharField(
        '描述',
        max_length=300
    )
    create_time = models.DateTimeField(
        '添加时间',
        auto_now_add=True
    )

    def __unicode__(self):
        return self.type_name

    class Meta:
        verbose_name = '维修类型'
        verbose_name_plural = verbose_name
