
from rest_framework import serializers
from django.db.models import Count, Case, Sum, When

from main.models import Order, Maintainer


class OrderSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        instance = super(OrderSerializer, self).create(validated_data)
        # 获取维修人员订单小于5的
        Maintainer.objects.aggregate(
            doing=Sum(
                Case(
                    When()
                )
            )
        )

    class Meta:
        model = Order
        fields = "__all__"
