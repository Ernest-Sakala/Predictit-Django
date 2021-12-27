from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DrugSerializer
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

    def put(self, request, pk, format=None):
        drug = DrugModel.objects.get(id=pk)
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


class FilterView(APIView):

    def get(self, request, disease, format=None):

        disease = DiseaseModel.objects.get(name=disease)

        drugs = DrugModel.objects.filter(disease=disease.id)

        serializer = DrugSerializer(drugs, many=True)

        return Response(serializer.data)


class PharmacyDrugView(APIView):

    def get(self, request, user_id, format=None):

        drugs = DrugModel.objects.filter(user=user_id)

        serializer = DrugSerializer(drugs, many=True)

        return Response(serializer.data)


class DrugByIdView(APIView):

    def get(self, request, pk, format=None):

        drug = DrugModel.objects.get(id=pk)
        serializer = DrugSerializer(drug)

        return Response(serializer.data)


class DeleteDrugView(APIView):

    def delete(self, request, drug_id, format=None):

        drug = DrugModel.objects.get(id=drug_id)
        drug.delete()
        return Response({"message": "Drug Deleted Successfully"})


