import datetime
import pickle
import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from api.settings import BASE_DIR
# new imports
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from custom_code import image_converter
from rest_framework.views import APIView
from disease.models import DiseaseModel
from rest_framework.response import Response
from rest_framework import status
from drug.serializers import DrugSerializer
from rest_framework.parsers import MultiPartParser
from .serializers import ImageSerializer
from drug.models import DrugModel


@api_view(['GET'])
def __index__function(request):
    start_time = datetime.datetime.now()
    elapsed_time = datetime.datetime.now() - start_time
    elapsed_time_ms = (elapsed_time.days * 86400000) + \
        (elapsed_time.seconds * 1000) + (elapsed_time.microseconds / 1000)
    return_data = {
        "error": "0",
        "message": "Successful",
        "restime": elapsed_time_ms
    }
    return HttpResponse(json.dumps(return_data), content_type='application/json; charset=utf-8')


def model_predict(img_path, model):
    print(img_path)
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    # Scaling
    x = x/255
    x = np.expand_dims(x, axis=0)

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
   # x = preprocess_input(x)

    preds = model.predict(x)
    preds = np.argmax(preds, axis=1)
    if preds == 0:
        preds = "Bacterial_spot"
    elif preds == 1:
        preds = "Early_blight"
    elif preds == 2:
        preds = "Late_blight"
    elif preds == 3:
        preds = "Leaf_Mold"
    elif preds == 4:
        preds = "Septoria_leaf_spot"
    elif preds == 5:
        preds = "Spider_mites Two-spotted_spider_mite"
    elif preds == 6:
        preds = "Target_Spot"
    elif preds == 7:
        preds = "Tomato_Yellow_Leaf_Curl_Virus"
    elif preds == 8:
        preds = "Tomato_mosaic_virus"
    else:
        preds = "Healthy"

    return preds


# @api_view(['POST', 'GET'])
# def predict_plant_disease(request):
    try:
        if request.method == "GET":
            return_data = {
                "error": "0",
                "message": "Plant Disease Detection Api. Does not accept GET request"
            }
        else:
            if request.body:
                request_data = request.data["plant_image"]
                header, image_data = request_data.split(';base64,')
                image_array, err_msg = image_converter.convert_image(
                    image_data)
                if err_msg == None:
                    model_file = f"{BASE_DIR}/ml_files/cnn_model.pkl"
                    saved_classifier_model = pickle.load(
                        open(model_file, 'rb'))
                    prediction = saved_classifier_model.predict(image_array)
                    label_binarizer = pickle.load(
                        open(f"{BASE_DIR}/ml_files/label_transform.pkl", 'rb'))
                    return_data = {
                        "error": "0",
                        "data": f"{label_binarizer.inverse_transform(prediction)[0]}"
                    }
                else:
                    return_data = {
                        "error": "4",
                        "message": f"Error : {err_msg}"
                    }
            else:
                return_data = {
                    "error": "1",
                    "message": "Request Body is empty",
                }
    except Exception as e:
        return_data = {
            "error": "3",
            "message": f"Error : {str(e)}",
        }
    return HttpResponse(json.dumps(return_data), content_type='application/json; charset=utf-8')


@api_view(['POST', 'GET'])
def predict_plant_disease(request):
    try:
        if request.method == "GET":
            return_data = {
                "error": "0",
                "message": "Plant Disease Detection Api. Does not accept GET request"
            }
        else:
            if request.body:
                request_data = request.FILES["plant_image"]

                MODEL_PATH = f"{BASE_DIR}/ml_files/model_inception.h5"

                model = load_model(MODEL_PATH)

                basepath = os.path.dirname(__file__)
                file_path = os.path.join(
                    basepath, 'uploads', request_data.name)
                request_data.save(file_path)

                preds = model_predict(file_path, model)
                result = preds

                return_data = {
                    "error": "0",
                    "data": f"{result}"
                }

            else:
                return_data = {
                    "error": "1",
                    "message": "Request Body is empty",
                }
    except Exception as e:
        return_data = {
            "error": "3",
            "message": f"Error : {str(e)}",
        }
    return HttpResponse(json.dumps(return_data), content_type='application/json; charset=utf-8')


class PredictView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)

        current_user = request.user

        if serializer.is_valid():
            serializer.save()

            MODEL_PATH = f"{BASE_DIR}/ml_files/model_inception.h5"

            model = load_model(MODEL_PATH)

            preds = model_predict(
                f"{BASE_DIR}/{serializer.data['image']}", model)
            result = preds

            disease = DiseaseModel.objects.get(name=result)

            drugs = DrugModel.objects.filter(disease=disease.id)

            serializer = DrugSerializer(drugs, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
