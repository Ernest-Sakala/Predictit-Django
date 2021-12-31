from django.shortcuts import render
from rest_framework.views import APIView
from .models import DiseaseModel
from rest_framework.response import Response
from .serializers import DieaseSerializer

# Create your views here.


class DiseaseView(APIView):

    def get(self, request, *args, **kwargs):

        diseases = DiseaseModel.objects.all()

        serializer = DieaseSerializer(diseases, many=True)

        return Response(serializer.data)
