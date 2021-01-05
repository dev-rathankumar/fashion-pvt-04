from django.urls import path
from . import views

urlpatterns = [
    path('rm-password-reset/', views.rm_password_reset, name="rm_password_reset" ),
    path('rm-password-reset-validate/<uidb64>/<token>/', views.rm_password_reset_validate, name='rm_password_reset_validate'),
]
