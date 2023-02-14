from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import CategoryModelViewSet, ProductModelViewSet
from shops.views import ShopModelViewSet, CurrencyModelViewSet, PaymentProvidersViewSet

router = DefaultRouter()
router.register('shop', ShopModelViewSet, 'shop')
router.register('category', CategoryModelViewSet, 'category')
router.register('currency', CurrencyModelViewSet, 'currency')
router.register('payment', PaymentProvidersViewSet, 'payment')

list_ = {'get': 'list', 'post': 'create'}
urlpatterns = [
    # path('shop/<int:pk>/order', ShopOrdersRetrieveAPIView.as_view(), name='orders'),
    path('', include(router.urls)),
    path('<int:pk>/product', ProductModelViewSet.as_view(list_), name='product-list'),
    path('<int:pk>/category', CategoryModelViewSet.as_view(list_), name='category-list')
]
