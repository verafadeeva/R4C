from django.contrib import admin

from robots.models import Robot


@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    list_display = ('id', 'serial', 'model', 'version', 'created')
    empty_value_display = '-пусто-'
