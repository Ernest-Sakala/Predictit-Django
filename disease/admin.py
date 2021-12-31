from django.contrib import admin
from .models import DiseaseModel
# Register your models here.


class DiseaseAdminConfig(admin.ModelAdmin):
    model = DiseaseModel
    list_display = ('id', 'name', 'description')


admin.site.register(DiseaseModel, DiseaseAdminConfig)
