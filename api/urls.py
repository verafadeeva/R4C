from django.urls import path

from api.views import robot_create


urlpatterns = [
    path('robot/create/', robot_create),
]
