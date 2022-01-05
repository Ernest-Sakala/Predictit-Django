from django.contrib import admin

from order.models import OrderModel

# Register your models here.


class OrderAdminConfig(admin.ModelAdmin):
    model = OrderModel
    list_display = ('id', 'pharmacy', 'paymentStatus', 'totalAmount')


admin.site.register(OrderModel, OrderAdminConfig)
