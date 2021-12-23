from rest_framework import serializers

from .models import PharmacyDetailModel


class PharmacyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacyDetailModel
        fields = ("__all__")
