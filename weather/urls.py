from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='dashboard'),
    path('delete/<str:city_name>/', delete, name='delete_city'),
]
