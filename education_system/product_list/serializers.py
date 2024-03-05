from rest_framework import serializers
from system.models import Product, Lesson


class ProductWithLessonCountSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(product=obj).count()
