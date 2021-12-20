from rest_framework import serializers
from .models import ProvinceModel


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvinceModel
        fields = ("__all__")
