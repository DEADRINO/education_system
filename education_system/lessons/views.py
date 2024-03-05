from rest_framework import generics
from system.models import Product
from .serializers import ProductSerializer


class LessonListByProduct(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Product.objects.filter(id=product_id)
