from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('users/', views.users_home, name='blog-users_home'),
    path('users/<slug:user>', views.users, name='blog-users'),
]