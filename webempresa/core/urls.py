from django.urls import path
from webempresa.core.views import home, about, store, contact, sample

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('store/', store, name='store'),
    path('contact/', contact, name='contact'),
    path('sample/', sample, name='sample'),
]
