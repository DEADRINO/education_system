from django.contrib import admin
from .models import Lesson, Product, Group, User
from django.contrib.auth.models import Permission


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'start_date', 'price']


class PermissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'content_type', 'codename']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'video_link']


class GroupAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'min_users', 'max_users']


admin.site.register(User)
admin.site.register(Product, ProductAdmin)
admin.site.register(Permission, PermissionAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Group, GroupAdmin)
