from django.contrib import admin
from .models import DrugModel

# Register your models here.


class DrugAdminConfig(admin.ModelAdmin):
    model = DrugModel
    list_display = ('id', 'name', 'disease', 'user', 'description')


admin.site.register(DrugModel, DrugAdminConfig)
