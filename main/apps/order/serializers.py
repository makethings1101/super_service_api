
from rest_framework import serializers
from django.db.models import Case, Sum, When, fields

from main.models import Order, Maintainer


class OrderSerializer(serializers.ModelSerializer):

    # 生成订单
    def create(self, validated_data):
        instance = super(OrderSerializer, self).create(validated_data)
        # 获取维修人员订单小于5的
        Maintainer.objects.annotate()
        maintainer_list = Maintainer.objects.annotate(
            doing=Sum(
                Case(
                    When(order__order_status=5, then=1),
                    default=0,
                    output_field=fields.IntegerField(),
                )
            )
        ).order_by('doing')

        for maintainer in maintainer_list:
            if maintainer.doing < 10:
                instance.wx_user = maintainer
                break
        instance.order_id = instance.make_order_id()
        instance.save()
        return instance

    class Meta:
        model = Order
        fields = (
            'wx_type',
            'user_remark',
            'repair_address'
        )
