from rest_framework import serializers
from .models import DiseaseModel


class DieaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseModel
        fields = ("__all__")
