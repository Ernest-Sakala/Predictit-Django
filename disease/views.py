from django.shortcuts import render
from rest_framework.views import APIView
from .models import DiseaseModel
from rest_framework.response import Response
from .serializers import DiseaseSerializer

# Create your views here.


class DiseaseView(APIView):

    def get(self, request, *args, **kwargs):

        diseases = DiseaseModel.objects.all()

        serializer = DiseaseSerializer(diseases, many=True)

        return Response(serializer.data)
