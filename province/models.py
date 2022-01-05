from django.db import models

# Create your models here.


class ProvinceModel(models.Model):

    class Meta:  # new
        verbose_name_plural = "Provinces"
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
