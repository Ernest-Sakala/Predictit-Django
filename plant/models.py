from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class ImageModel(models.Model):
    image = models.ImageField(
        _('Image'), upload_to=upload_to, default='images/default.jpg')
