from django.conf import settings
from django.db import models
from address.models import AddressModel
# Create your models here.


class OrderModel(models.Model):
    pharmacy = models.IntegerField()
    paymentStatus = models.BooleanField()
    orderedDate = models.DateTimeField()
    packedDate = models.DateTimeField()
    transportedDate = models.DateTimeField()
    deliveredDate = models.DateTimeField()
    cancelledDate = models.DateTimeField()
    deliveryPrice = models.DateTimeField()
    orderStatus = models.CharField()
    totalAmount = models.CharField()
    totalProducts = models.IntegerField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE)
