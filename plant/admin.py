from django.contrib import admin
from .models import ImageModel

# Register your models here.


class ImageAdminConfig(admin.ModelAdmin):
    model = ImageModel
    list_display = ('id', 'image')


admin.site.register(ImageModel, ImageAdminConfig)
