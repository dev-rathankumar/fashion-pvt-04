from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.banners),
    # Header
    path('header/', views.header, name='header'),
    path('header/add/', views.headerAdd, name='headerAdd'),
    path('header/edit/<int:pk>/', views.headerEdit, name='headerEdit'),
    # Banners
    path('banners/', views.banners, name='banners'),
    path('banners/addBanner/', views.addBanner, name='addBanner'),
    path('banners/editBanner/<int:pk>/', views.editBanner, name='editBanner'),
    path('banners/deleteBanner/<int:pk>/', views.deleteBanner, name='deleteBanner'),

    # Store features
    path('store_features/', views.store_features, name='store_features'),
    path('store_features/addFeature/', views.addFeature, name='addFeature'),
    path('store_features/editFeature/<int:pk>/', views.editFeature, name='editFeature'),
    path('store_features/deleteFeature/<int:pk>/', views.deleteFeature, name='deleteFeature'),

    # Homepage Background
    path('homepage_background/', views.homepage_background, name='homepage_background'),

    # About Us

    # Contact Us
    path('contactUs/', views.contactUs, name='contactUs'),

    # Footer
    path('footerEdit/', views.footerEdit, name='footerEdit'),

    # Social Icons
    path('socialIcons/', views.socialIcons, name='socialIcons'),
    path('socialIcons/addIcon/', views.addIcon, name='addIcon'),
    path('socialIcons/editIcon/<int:pk>/', views.editIcon, name='editIcon'),
    path('socialIcons/deleteIcon/<int:pk>/', views.deleteIcon, name='deleteIcon'),

]
