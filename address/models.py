from django.conf import settings
from django.db import models
from province.models import ProvinceModel
from town.models import TownModel

# Create your models here.


class AddressModel(models.Model):
    fullName = models.CharField()
    address = models.CharField()
    mobileNumber = models.CharField()
    alternateNumber = models.CharField()
    selected = models.BooleanField()
    compound = models.CharField()
    buldingNumber = models.CharField()
    landMark = models.CharField()

    town = models.ForeignKey(TownModel, on_delete=models.CASCADE)
    province = models.ForeignKey(ProvinceModel, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
