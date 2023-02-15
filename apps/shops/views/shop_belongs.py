from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shared.permisions import IsAdminOrReadOnly
from shared.validators import TelegramBotValidator
from shops.models import Currency, Category, TelegramBot, PaymentProvider
from shops.serializers import CategorySerializer, CurrencySerializer, PaymentSerializers, TelegramBotModelSerializer


class CategoryModelViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class CurrencyModelViewSet(ModelViewSet):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class PaymentProvidersViewSet(ModelViewSet):
    serializer_class = PaymentSerializers
    queryset = PaymentProvider.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


# class ShopOrdersRetrieveAPIView(RetrieveAPIView):
#     serializer_class = OrderSerializer
#     pagination_class = LimitOffsetPagination
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#         shop: Shop = self.get_object()
#         return shop.order_set.all()

class TelegramBotModelViewSet(ModelViewSet):
    serializer_class = TelegramBotModelSerializer
    queryset = TelegramBot.objects.all()
    permission_classes = AllowAny,

    def update(self, request, *args, **kwargs):
        token = request.data.get('token')
        validate = TelegramBotValidator()
        bot = validate(token, **kwargs)
        if bot.get('data'):
            return Response(bot['data'], status=bot['status'])
        shop = bot['shop']
        bot, _ = TelegramBot.objects.update_or_create(shop=shop, defaults=bot)
        serializer = TelegramBotModelSerializer(bot)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
