from django.contrib import admin

from address.models import AddressModel


# Register your models here.

class AddressAdminConfig(admin.ModelAdmin):
    model = AddressModel
    list_display = ('id', 'address', 'fullName',
                    'town', 'province', 'compound')


admin.site.register(AddressModel, AddressAdminConfig)
