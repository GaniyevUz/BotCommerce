from django.db.models import Count
from django.db.models.expressions import RawSQL
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from orders.models import Order
from shared.paginate import CountResultPaginate
from shared.permisions import IsAuthenticatedOwner
from shops.models import Shop
from shops.models.shop_belongs import PaymentProvider
from shops.serializers import ShopSerializer, PaymentSerializers


class ShopModelViewSet(ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    pagination_class = CountResultPaginate
    permission_classes = IsAuthenticatedOwner,

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(user=request.user)
        return super().list(request, *args, **kwargs)

    @action(['GET'], False)
    def shop_config(self, request):
        langs = (("🇺🇿", "O'zbekcha", "uz"), ("🇷🇺", "Русский", "ru"), ("🇺🇸", "English", "en"))
        data = {"languages": [{'icon': i, 'title': t, 'code': c} for i, t, c in langs]}
        return Response(data)

    # Todo: Muhammad bro classga olib chiqib ketin
    @action(['GET'], True, 'stat/all', 'stat_all')
    def main_stat(self, request, pk=None):
        orders = Order.objects.filter(items__order__shop_id=pk).annotate(total_items=Count('items'))
        total_orders = sum(orders.values_list('total_items', flat=True))

        paid_orders = orders.filter(paid=True).annotate(total_items=Count('items'))
        paid_orders_cost = sum(paid_orders.values_list('total_items', flat=True))

        _ = Order.objects.values('id').annotate(summ=RawSQL("SELECT get_summ_all(%s)", (1,)),
                                                avg=RawSQL("SELECT get_avarage_price(%s)", (1,)))[0]
        revenue, avg = _['summ'], _['avg']
        # total_customers = Client.objects.filter(shop_id=pk).count() # client chala
        data = {
            'id': pk,
            'total_orders': total_orders,
            'paid_orders': paid_orders_cost,
            'total_revenue': revenue,
            'total_customers': 'chala',
            'average_price': avg
        }
        return Response(data)


class PaymentProvidersListAPIView(ListAPIView):
    queryset = PaymentProvider.objects.all()
    serializer_class = PaymentSerializers
