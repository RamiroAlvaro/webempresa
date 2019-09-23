from django.urls import path
from webempresa.core.views import home, about, services, store, contact, sample, blog

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('store/', store, name='store'),
    path('contact/', contact, name='contact'),
    path('sample/', sample, name='sample'),
    path('blog/', blog, name='blog'),
]
