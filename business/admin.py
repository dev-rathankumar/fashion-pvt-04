from django.contrib import admin
from django.utils.html import format_html
from .models import SiteSetting, TestRathan


# Register your models here.
class SiteSettingAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius: 50px;" />'.format(object.site_logo.url))

    thumbnail.short_description = 'Logo'
    list_display = ('thumbnail', 'business', 'site_title')
    list_display_links = ('thumbnail', 'business', 'site_title')
    
    fields = ('business', 'site_title', 'site_logo', 'copyright')

    def get_business(self, obj):
        return obj.business.company_name
    get_business.short_description = 'Business'
    get_business.admin_order_field = 'user__name'


class TestRathanAdmin(admin.ModelAdmin):
    list_display = ('business_test', 'site_title')

admin.site.register(SiteSetting, SiteSettingAdmin)
admin.site.register(TestRathan, TestRathanAdmin)
