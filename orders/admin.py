from django.contrib import admin
from .models import Order, OrderProduct, Payment



class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'variant', 'color', 'size', 'price', 'quantity', 'amount')
    can_delete = False
    extra = 0

class OrderInline(admin.TabularInline):
    model = Order
    fields = ['order_number', 'name', 'phone', 'email', 'total', 'tax', 'status', 'ordered', 'created_at']
    readonly_fields = ['order_number', 'name', 'phone', 'email', 'city', 'total', 'tax', 'status', 'ordered', 'created_at']
    can_delete = False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'name', 'phone', 'email', 'city', 'total', 'tax', 'status', 'ordered', 'created_at']
    list_filter = ['status', 'ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    readonly_fields = ('payment','user', 'order_number', 'total', 'tax', 'ip', 'note')
    list_per_page = 100
    can_delete = False
    inlines = [OrderProductInline]


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'variant', 'color', 'size', 'price', 'quantity', 'amount', 'ordered']
    list_filter = ['user']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'payment_method', 'payment_id', 'amount', 'status', 'created_at']
    readonly_fields = ('user', 'payment_id', 'amount', 'status', 'created_at')
    inlines = [OrderInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)
admin.site.register(Payment, PaymentAdmin)
