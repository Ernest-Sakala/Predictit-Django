from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from order.models import OrderModel
from order.serializers import OrderSerializer

# Create your views here.


class OrderView(APIView):

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):

        order = OrderModel.objects.filter(user=request.user.id)
        serializer = OrderSerializer(order, many=True)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):

        id = request.query_params["id"]

        order = OrderModel.objects.get(id=id)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):

        id = request.query_params["id"]

        order = OrderModel.objects.get(id=id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PharmacyOrderView(APIView):

    def get(self, request, *args, **kwargs):

        order = OrderModel.objects.filter(pharmacy=request.user.id)
        serializer = OrderSerializer(order, many=True)

        return Response(serializer.data)
