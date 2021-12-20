from rest_framework import serializers
from .models import DrugModel


class DrugSerializer(serializers.ModelSerializer):

    class Meta:
        model = DrugModel
        exclude = ['user']
        #fields = '__all__'
