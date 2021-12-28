from django.shortcuts import render
from rest_framework.views import APIView
from .models import ProvinceModel
from rest_framework.response import Response
from .serializers import ProvinceSerializer

# Create your views here.


class ProvinceView(APIView):

    def get(self, request, *args, **kwargs):

        provinces = ProvinceModel.objects.all()

        serializer = ProvinceSerializer(provinces, many=True)

        return Response(serializer.data)
