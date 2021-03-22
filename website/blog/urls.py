from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('tags/', views.tags_home, name='blog-tags_home'),
    path('tags/<slug:tag>', views.tags, name='blog-tags'),
    path('users/', views.users_home, name='blog-users_home'),
    path('users/<slug:user>', views.users, name='blog-users'),
]