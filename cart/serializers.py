from rest_framework import serializers
from .models import CartModel
from drug.models import DrugModel


class CartSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = CartModel
        fields = ('id', 'drug', 'quantity')


class CartSerializerRead(serializers.ModelSerializer):

    class Meta:
        model = CartModel
        fields = ("__all__")
        depth = 1


class CartSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = CartModel
        fields = ('id', 'drug', 'quantity')
