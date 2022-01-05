from django.contrib import admin

from cart.models import CartModel

# Register your models here.


class CartAdminConfig(admin.ModelAdmin):
    model = CartModel
    list_display = ('id', 'quantity')


admin.site.register(CartModel, CartAdminConfig)
