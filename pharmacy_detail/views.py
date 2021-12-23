from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PharmacyDetailSerializer
from rest_framework.response import Response
from .models import PharmacyDetailModel
# Create your views here.


class PharmacyDetailView(APIView):

    def post(self, request):
        serializer = PharmacyDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):

        order = PharmacyDetailModel.objects.filter(
            request.user.id)
        serializer = PharmacyDetailSerializer(order, many=True)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = PharmacyDetailSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
