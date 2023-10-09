from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'robot_serial', 'is_done')
    empty_value_display = '-пусто-'
