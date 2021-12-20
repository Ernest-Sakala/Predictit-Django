from rest_framework import serializers
from .models import TownModel


class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = TownModel
        fields = ("__all__")
