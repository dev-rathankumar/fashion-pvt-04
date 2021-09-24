from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.emails, name='emails'),
    path('send_email', views.send_email, name='send_email'),
    path('email_detail/<int:pk>/', views.email_detail, name='email_detail'),
    path('email_settings/', views.email_settings, name='email_settings'),
    path('email_settings/test_mail/', views.test_mail, name='test_mail'),
    path('emailContactList/', views.emailContactList, name='emailContactList'),
    path('deleteSubscriber/<int:pk>/', views.deleteSubscriber, name='deleteSubscriber'),
    
]
