from rest_framework import serializers
from plant.models import ImageModel


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ("__all__")
