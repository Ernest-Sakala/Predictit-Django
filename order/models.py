from django.conf import settings
from django.db import models
from address.models import AddressModel
# Create your models here.


class OrderModel(models.Model):
    pharmacy = models.IntegerField()
    paymentStatus = models.BooleanField()
    orderedDate = models.DateTimeField(auto_now_add=True)
    packedDate = models.DateTimeField(auto_now_add=True)
    transportedDate = models.DateTimeField(auto_now_add=True)
    deliveredDate = models.DateTimeField(auto_now_add=True)
    cancelledDate = models.DateTimeField(auto_now_add=True)
    deliveryPrice = models.CharField(max_length=255)
    orderStatus = models.CharField(max_length=255)
    totalAmount = models.CharField(max_length=255)
    totalProducts = models.IntegerField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE)
