from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (CartSerializerCreate,  CartSerializerRead)
from .models import CartModel
from django.http import Http404
# Create your views here.


class CartView(APIView):

    def post(self, request):
        serializer = CartSerializerCreate(data=request.data)
        if serializer.is_valid():
            try:
                cart = CartModel.objects.get(
                    user=request.user.id, drug=serializer.validated_data.get('drug'))

                if cart is not None:
                    return Response({"message ": "Item already added to cart"})

            except CartModel.DoesNotExist:
                serializer.save(user=self.request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):

        cart = CartModel.objects.filter(
            user=request.user.id).select_related('drug')

        if not cart:
            return Response({"message": "You have no drugs in cart"})

        serializer = CartSerializerRead(cart, many=True)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):

        id = request.query_params["id"]

        cart = CartModel.objects.get(id=id)
        serializer = CartSerializerCreate(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):

        id = request.query_params["id"]

        try:
            cart = CartModel.objects.get(id=id)
        except CartModel.DoesNotExist:
            return Response({"message": "Item does not exist"})

        cart.delete()
        return Response({"message": "Item deleted Successfully"})
