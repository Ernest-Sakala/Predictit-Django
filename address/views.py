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

    def get(self, request, pk, format=None):

        address = AddressModel.objects.filter(
            request.user.id)
        serializer = AddressSerializer(address, many=True)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        address = self.get_object(pk)
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        address = self.get_object(pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
