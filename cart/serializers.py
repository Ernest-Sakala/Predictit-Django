from rest_framework import serializers
from .models import CartModel
from drug.models import DrugModel


class CartSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = CartModel
        fields = ("__all__")


class CartSerializerRead(serializers.ModelSerializer):

    class Meta:
        model = CartModel
        fields = ("__all__")
        depth = 1
