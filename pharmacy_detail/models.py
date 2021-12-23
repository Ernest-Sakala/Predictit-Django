from django.conf import settings
from django.db import models
from province.models import ProvinceModel
from town.models import TownModel
from django.utils.translation import gettext_lazy as _


# Create your models here.


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class PharmacyDetailModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    province = models.ForeignKey(ProvinceModel, on_delete=models.CASCADE)
    town = models.ForeignKey(TownModel, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    image = models.ImageField(
        _('Image'), upload_to=upload_to, default='images/default.jpg')
