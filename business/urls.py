from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='biz_dashboard'),
    path('login/', views.login, name='biz_login'),
    path('logout/', views.logout, name='biz_logout'),

    path('forgotPassword/', views.forgotPassword, name='biz_forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='biz_resetForgotPassword_validate'),
    path('resetPassword/', views.biz_resetPassword, name='biz_resetForgotPassword'),

    path('profile/', views.biz_profile, name='biz_profile'),
    path('changePassword/', views.biz_changePassword, name='biz_changePassword'),

    # Edit profile
    path('editProfile/<int:pk>/', views.editProfile, name='editProfile'),

    # Payment settings
    path('paymentSettings/<int:pk>/', views.paymentSettings, name='paymentSettings'),

    # Categories
    path('categories/', views.allCategories, name='allCategories'),
    path('categories/addCategory/', views.addCategory, name='addCategory'),

    # Products
    path('products/', views.allProducts, name='allProducts'),
    path('products/editProduct/<int:pk>/', views.editProduct, name='editProduct'),
    path('products/editProduct/<int:pk>/editGallery/', views.editGallery, name='editGallery'),
    path('products/editProduct/<int:pk>/editVariants/', views.editVariants, name='editVariants'),
    path('products/addProduct/', views.addProduct, name='addProduct'),
    path('products/deleteProduct/<int:pk>/', views.deleteProduct, name='deleteProduct'),

    # Site settings
    path('site_settings/', include('sitesettings.urls')),



]
