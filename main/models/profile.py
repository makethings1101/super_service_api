# coding:utf-8

from django.db import models


class CustomerProfile(models.Model):
    user = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE
    )
    phone = models.CharField(
        '手机号',
        max_length=15,
        default=''
    )

    address = models.CharField(
        '地址',
        max_length=20,
        help_text='例如:2栋2单元401'
    )
    name = models.CharField(
        '用户姓名',
        max_length=20
    )

    class Meta:
        verbose_name = '使用者详情'
        verbose_name_plural = verbose_name


class Maintainer(models.Model):
    # 维修人员
    user = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        '姓名',
        max_length=20,
        help_text='维修师傅姓名'
    )
    phone = models.CharField(
        '手机号',
        max_length=20
    )

    class Meta:
        verbose_name = '维修人员'
        verbose_name_plural = verbose_name


class Property(models.Model):
    # 物管人员
    user = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        '姓名',
        max_length=20,
        help_text='物管名称'
    )

    phone = models.CharField(
        '手机号',
        max_length=20,
        default=''
    )

    tel = models.CharField(
        '座机号',
        max_length=20,
        default=''
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '物管名称'
        verbose_name_plural = verbose_name
