from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view, name='login'),
    path('create_product/',
         views.CreatePostView.as_view,
         name='create_product'),
]
