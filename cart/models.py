from django.db import models
from django.conf import settings
from drug.models import DrugModel

# Create your models here.


class CartModel(models.Model):
    drug = models.ForeignKey(DrugModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
