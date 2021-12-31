from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PharmacyDetailSerializer
from rest_framework.response import Response
from .models import PharmacyDetailModel
# Create your views here.


class PharmacyDetailView(APIView):

    parser_classes = [MultiPartParser]

    def post(self, request):
        serializer = PharmacyDetailSerializer(data=request.data)
        if serializer.is_valid():

            try:
                cart = PharmacyDetailModel.objects.get(user=request.user.id)

                if cart is not None:
                    return Response({"message ": "Details already added"})

            except PharmacyDetailModel.DoesNotExist:
                serializer.save(user=self.request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):

        detail = PharmacyDetailModel.objects.filter(user=request.user.id)
        serializer = PharmacyDetailSerializer(detail, many=True)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):

        id = request.query_params["id"]

        detail = PharmacyDetailModel.objects.get(id=id)

        serializer = PharmacyDetailSerializer(detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):

        id = request.query_params["id"]

        detail = PharmacyDetailModel.objects.get(id=id)
        detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PharmacyDetails(APIView):

    def get(self, request, *args, **kwargs):

        id = request.query_params["id"]

        detail = PharmacyDetailModel.objects.get(user=id)

        serializer = PharmacyDetailSerializer(detail)

        return Response(serializer.data)
