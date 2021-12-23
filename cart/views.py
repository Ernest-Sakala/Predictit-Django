from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CartSerializer
from .models import CartModel
# Create your views here.


class CartView(APIView):

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):

        cart = CartModel.objects.filter(
            user=request.user.id).select_related('drug')
        serializer = CartSerializer(cart, many=True)

        return Response(serializer.data)

    def put(self, request, pk, format=None):

        cart = CartModel.objects.get(id=pk)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cart = CartModel.objects.get(id=pk)
        cart.delete()
        return Response({"message": "Item deleted Successfully"})
