from system.models import Product
from .serializers import ProductWithLessonCountSerializer
from rest_framework import generics


class ProductListByProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWithLessonCountSerializer
