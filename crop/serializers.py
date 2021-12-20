from rest_framework import serializers
from .models import CropModel


class CropSerializer(serializers.Serializer):
    class Meta:
        model = CropModel
        fields = ('name')
