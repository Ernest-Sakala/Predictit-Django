from rest_framework import serializers
from .models import DieaseModel


class DieaseSerializer(serializers.Serializer):
    model = DieaseModel
    fields = ('id', 'name')
