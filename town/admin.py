from django.contrib import admin
from .models import TownModel

# Register your models here.


class TownAdminConfig(admin.ModelAdmin):
    model = TownModel
    list_display = ('id', 'name', 'province')


admin.site.register(TownModel, TownAdminConfig)
