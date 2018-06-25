
from rest_framework import mixins, viewsets

from main.apps.order.serializers import OrderSerializer
from main.models import Order


class OrderViews(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.UpdateModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.filter

    # 用户订单管理中心。包含创建，查看更新。
    def get_queryset(self):
        query_set = super(OrderViews, self).get_queryset()
        return query_set.filter(customer=self.request.user.customerprofile)

    def perform_create(self, serializer):
        serializer.save()
        serializer.customer = self.request.user.customerprofile
        serializer.save()
