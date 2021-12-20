from django.conf import settings
from django.db import models
from drug.models import DrugModel
from order.models import OrderModel

# Create your models here.


class OrderDrug(models.Model):
    drug = models.ForeignKey(DrugModel, on_delete=models.CASCADE)
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
