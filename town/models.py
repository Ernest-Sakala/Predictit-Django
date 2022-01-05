from django.db import models
from province.models import ProvinceModel

# Create your models here.


class TownModel(models.Model):

    class Meta:  # new
        verbose_name_plural = "Towns"

    name = models.CharField(max_length=255, unique=True)
    province = models.ForeignKey(ProvinceModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
