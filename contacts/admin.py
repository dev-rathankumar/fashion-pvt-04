from django.contrib import admin
from .models import Inquiry


class InquiryAdmin(admin.ModelAdmin):
    list_display = ('business', 'first_name', 'last_name', 'product_name', 'email', 'create_date')
    list_display_links = ('business', 'first_name', 'last_name', 'product_name', 'email')

admin.site.register(Inquiry, InquiryAdmin)
