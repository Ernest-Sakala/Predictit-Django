from django.shortcuts import render
from rest_framework.views import APIView
from .models import OrderDrug
from rest_framework import status
from .serializers import OrderDrugSerializer
from rest_framework.response import Response
# Create your views here.


class OrderDrugView(APIView):

    def post(self, request):
        serializer = OrderDrugSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):

        order = OrderDrug.objects.filter(
            request.user.id)
        serializer = OrderDrugSerializer(order, many=True)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderDrugSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
