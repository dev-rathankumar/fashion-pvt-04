from django.contrib import admin
from .models import Order, OrderProduct



class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'variant', 'color', 'size', 'price', 'quantity', 'amount')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'name', 'phone', 'email', 'city', 'total', 'tax', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    readonly_fields = ('user', 'order_number', 'address_line_1', 'address_line_2', 'ip', 'note')
    can_delete = False
    inlines = [OrderProductInline]


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'variant', 'color', 'size', 'price', 'quantity', 'amount']
    list_filter = ['user']



admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)
