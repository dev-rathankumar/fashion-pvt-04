from django.contrib import admin
from .models import Header, Footer, ContactPage
import admin_thumbnails


class HeaderAdmin(admin.ModelAdmin):
    list_display = ['business', 'site_title']


admin.site.register(Header, HeaderAdmin)
admin.site.register(Footer)
admin.site.register(ContactPage)
