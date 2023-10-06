from django.urls import path

from api.views import robot_create, export_excel_file


urlpatterns = [
    path('robot/create/', robot_create),
    path('report/', export_excel_file),
]
