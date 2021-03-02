from django.urls import path, include
from . import views

urlpatterns = [
    path('header/', views.header, name='header'),
    path('header/add/', views.headerAdd, name='headerAdd'),
    path('header/edit/<int:pk>/', views.headerEdit, name='headerEdit'),
]
