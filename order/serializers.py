from rest_framework import serializers

from order.models import OrderModel


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        exclude = ['user']
