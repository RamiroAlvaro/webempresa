from django.urls import path
from webempresa.contact.views import contact

urlpatterns = [
    path('', contact, name='contact'),
]