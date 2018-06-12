import datetime

from django.db import models


class Order(models.Model):
    ORDER_STATUS = (
        (10, '等待分配'),
        (20, '等待接单'),
        (30, '等待维修'),
        (40, '加急'),
        (50, '维修中'),
        (60, '维修完成'),
        (70, '评价'),
        (80, '取消'),
    )
    GRADE = (
        (0, '一星'),
        (1, '两星'),
        (2, '三星'),
        (3, '四星'),
        (4, '五星'),
    )
    order_id = models.CharField(
        '订单号',
        max_length=32,
        default='',
        blank=True
    )
    customer = models.ForeignKey(
        'main.CustomerProfile',
        on_delete=models.CASCADE,
        blank=True
    )
    wx_type = models.ForeignKey(
        'main.WxType',
        on_delete=models.CASCADE
    )
    user_remark = models.CharField(
        '用户报修描述',
        max_length=200,
        blank=True,
        default=''
    )
    repair_address = models.CharField(
        '用户报修地址',
        max_length=30,
        help_text='默认拉去用户的地址,如果没有就需要用户填写'
    )
    order_status = models.IntegerField(
        '订单状态',
        choices=ORDER_STATUS,
        default=10,
    )
    cancel_remark = models.CharField(
        '取消备注',
        max_length=200,
        default='',
        blank=True
    )
    user_grade = models.IntegerField(
        '用户评分',
        choices=GRADE,
        blank=True,
        help_text='用户评价等级'
    )
    user_evaluate = models.CharField(
        '用户评价',
        max_length=200,
    )
    wx_user = models.ForeignKey(
        'main.Maintainer',
        on_delete=models.CASCADE,
        blank=True
    )

    def __unicode__(self):
        return self.order_id

    def make_order_id(self):
        # 生成订单号
        return '%s%8.8d' % (datetime.date.today().strftime('%Y%m%d'), self.id)

    class Meta:
        verbose_name = '报修订单'
        verbose_name_plural = verbose_name
