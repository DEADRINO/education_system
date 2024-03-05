from django.urls import path, include
from rest_framework import routers
from product_list.views import ProductListByProduct


urlpatterns = [
    path('products/', ProductListByProduct.as_view(),
         name='product_with_lesson_count'),
]
