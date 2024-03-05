from django.urls import path
from .views import LessonListByProduct

urlpatterns = [
    path('<int:product_id>/lessons/',
         LessonListByProduct.as_view(), name='lesson-list-by-product'),
]
