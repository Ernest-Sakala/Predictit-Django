from django.shortcuts import render
from rest_framework.views import APIView
from .models import TownModel
from rest_framework.response import Response
from .serializers import TownSerializer

# Create your views here.


class TownView(APIView):

    def get(self, request, *args, **kwargs):

        towns = TownModel.objects.all()

        serializer = TownSerializer(towns, many=True)

        return Response(serializer.data)
