from django.db import models
from crop.models import CropModel

# Create your models here.


class DiseaseModel(models.Model):

    class Meta:  # new
        verbose_name_plural = "Diseases"

    crop = models.ForeignKey(CropModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
