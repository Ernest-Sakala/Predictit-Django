from rest_framework import serializers
from .models import AddressModel


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        exclude = ['user']
