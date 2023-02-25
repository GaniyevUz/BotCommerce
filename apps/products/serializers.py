from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer
from products.models import Product, Category


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = 'lft', 'rght', 'level', 'tree_id', 'shop'


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = 'rght', 'lft', 'tree_id', 'level'


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryMoveSerializer(ModelSerializer):
    position = IntegerField()

    class Meta:
        model = Category
        fields = ('position',)
