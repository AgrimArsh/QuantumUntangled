from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users_home, name='blog-users_home'),
    path('users/<slug:user>', views.users, name='blog-users'),
]