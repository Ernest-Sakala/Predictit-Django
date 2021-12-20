from django.contrib import admin
from .models import ProvinceModel
# Register your models here.


class ProvinceAdminConfig():
    model = ProvinceModel
    list_display = ('id', 'name')


admin.site.register(ProvinceModel, ProvinceAdminConfig)
