from django.contrib import admin
from .models import CropModel

# Register your models here.


class CropAdminConfig(admin.ModelAdmin):
    model = CropModel
    list_display = ('id', 'name')


admin.site.register(CropModel, CropAdminConfig)
