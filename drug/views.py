from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (DrugSerializer, DrugSerializerGet)
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from .models import DrugModel
from rest_framework import generics
from disease.models import DiseaseModel
import json
# Create your vie ws here.


class DrugView(APIView):

    parser_classes = [MultiPartParser]

    def post(self, request):
        serializer = DrugSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,  *args, **kwargs):

        id = request.query_params["id"]

        drug = DrugModel.objects.get(id=id)
        serializer = DrugSerializer(drug, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):

        user = request.user

        drugs = DrugModel.objects.filter(user=user.id)

        serializer = DrugSerializer(drugs, many=True)

        return Response(serializer.data)

# 
class FilterView(APIView):

    def get(self, request, *args, **kwargs):

        disease_name = request.query_params["disease"]

        disease = DiseaseModel.objects.get(name=disease_name)

        drugs = DrugModel.objects.filter(disease=disease.id)

        serializer = DrugSerializer(drugs, many=True)

        return Response(serializer.data)


class PharmacyDrugView(APIView):

    def get(self, request, *args, **kwargs):

        id = request.query_params["id"]

        drugs = DrugModel.objects.filter(user=id)

        serializer = DrugSerializer(drugs, many=True)

        return Response(serializer.data)


class DrugByIdView(APIView):

    def get(self, request, *args, **kwargs):

        pk = request.query_params["id"]

        drug = DrugModel.objects.get(id=pk)

    
        serializer = DrugSerializerGet(drug)

        return Response(serializer.data)


class DeleteDrugView(APIView):

    def delete(self, request, *args, **kwargs):

        id = request.query_params["id"]

        drug = DrugModel.objects.get(id=id)
        drug.delete()
        return Response({"message": "Drug Deleted Successfully"})
