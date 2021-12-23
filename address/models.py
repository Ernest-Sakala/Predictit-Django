from django.conf import settings
from django.db import models
from province.models import ProvinceModel
from town.models import TownModel

# Create your models here.


class AddressModel(models.Model):
    fullName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mobileNumber = models.CharField(max_length=255)
    alternateNumber = models.CharField(max_length=255, blank=True)
    selected = models.BooleanField(default=False)
    compound = models.CharField(max_length=255)
    buldingNumber = models.CharField(max_length=255, blank=True)
    landMark = models.CharField(max_length=255)

    town = models.ForeignKey(TownModel, on_delete=models.CASCADE)
    province = models.ForeignKey(ProvinceModel, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
