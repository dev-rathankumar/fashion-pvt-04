from django.urls import path
from . import views


urlpatterns = [
    path('orderproduct/', views.orderproduct, name='orderproduct'),
    path('order_complete/', views.order_complete, name='order_complete'),
]
