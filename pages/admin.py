from django.contrib import admin
from .models import Team, About, Contact
from django.utils.html import format_html


# Team Admin
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius: 50px;" />'.format(object.photo.url))
    thumbnail.short_description = 'Photo'
    list_display = ('thumbnail', 'business', 'name', 'designation', 'is_active', 'created_date')
    list_display_links = ('thumbnail', 'business', 'name', 'designation')
    list_editable = ('is_active',)
    search_fields = ('id', 'first_name', 'last_name', 'designation')
    list_filter = ('business', 'is_active')


# About Admin
class AboutAdmin(admin.ModelAdmin):
    list_display = ('get_business_id', 'business')
    list_display_links = ('get_business_id', 'business')
    search_fields = ('id', 'business__business_id', 'business')

    def get_business_id(self, obj):
        return obj.business.business_id
    get_business_id.short_description = 'Business ID'
    get_business_id.admin_order_field = 'business__business_id'

# Contact Admin
class ContactAdmin(admin.ModelAdmin):
    list_display = ('get_business_id', 'business', 'name', 'email', 'phone', 'contacted_date')
    list_display_links = ('get_business_id', 'business', 'name', 'email', 'phone')
    search_fields = ('id', 'business__business_id', 'business', 'name', 'email', 'phone')

    def get_business_id(self, obj):
        return obj.business.business_id
    get_business_id.short_description = 'Business ID'
    get_business_id.admin_order_field = 'business__business_id'

# Register your models.
admin.site.register(Team, TeamAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Contact, ContactAdmin)
