from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),


    # Site settings
    path('site-settings/', views.site_settings, name='site_settings'),
    path('site-settings/create/', views.site_settings_create, name='site_settings_create'),
]
