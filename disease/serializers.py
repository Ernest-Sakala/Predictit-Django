from rest_framework import serializers
from .models import DieaseModel


class DieaseSerializer(serializers.Serializer):
    class Meta:
        model = DieaseModel
        fields = ('id', 'name')
