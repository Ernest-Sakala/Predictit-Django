from django.db import models
from disease.models import DiseaseModel
from user.models import CustomUser
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Create your models here.


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


# Create your models here.


class DrugModel(models.Model):
    disease = models.ForeignKey(
        DiseaseModel, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(
        _('Image'), upload_to=upload_to, default='images/default.jpg')
