from django.contrib import admin
from .models import Cart, CartItem, Tax, ShopCart

class TaxAdmin(admin.ModelAdmin):
    def tax_percent(self, object):
        return object.tax_percentage
    tax_percent.short_description = 'Tax (%)'
    list_display = ('business', 'tax_percent')


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product','user','quantity','price','amount', 'size', 'color' ]
    list_filter = ['user']


admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(Tax, TaxAdmin)
