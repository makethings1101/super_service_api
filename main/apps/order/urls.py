from rest_framework.routers import DefaultRouter
from main.apps.order.views import OrderViews

router = DefaultRouter()

router.register('order', OrderViews, base_name='order')

urlpatterns = router.urls