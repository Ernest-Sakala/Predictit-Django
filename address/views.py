from django.shortcuts import render
from rest_framework.views import APIView
from address.models import AddressModel
from rest_framework import status
from rest_framework.response import Response
from address.serializers import AddressSerializer

# Create your views here.


class AddressView(APIView):

    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):

        addresses = AddressModel.objects.filter(user=request.user.id)

        if not addresses:
            return Response({"message": "You have no addresses"})

        serializer = AddressSerializer(addresses, many=True)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):

        id = request.query_params["id"]

        address = AddressModel.objects.get(id=id)

        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):

        id = request.query_params["id"]

        try:
            address = AddressModel.objects.get(id=id)

        except AddressModel.DoesNotExist:
            return Response({"message": "Item does not exist"})

        address.delete()
        return Response({"message": "Item deleted Successfully"})
