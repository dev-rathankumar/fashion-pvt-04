from django.urls import path
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

]
