from django.urls import path
from webempresa.blog.views import blog, category

urlpatterns = [
    path('', blog, name='blog'),
    path('category/<int:category_id>/', category, name='category'),
]
