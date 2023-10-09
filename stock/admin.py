from django.contrib import admin

from stock.models import Stock


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'robot_serial', 'amount')
    empty_value_display = '-пусто-'
