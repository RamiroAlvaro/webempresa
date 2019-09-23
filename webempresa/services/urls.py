from django.urls import path
from webempresa.services.views import services

urlpatterns = [
    path('', services, name='services'),
]