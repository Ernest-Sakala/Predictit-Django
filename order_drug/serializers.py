from rest_framework import serializers

from .models import OrderDrug


class OrderDrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDrug
        fields = ("__all__")
