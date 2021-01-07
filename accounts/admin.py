from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Customer, Country, State, Business, RegionalManager
from django.utils.html import format_html


# User Admin
class UserAdmin(UserAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius: 50px;" />'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'

    list_display = ('thumbnail', 'email', 'name', 'username', 'is_customer', 'is_business', 'is_regional_manager', 'is_active')
    list_display_links = ('email', 'name', 'username')
    list_editable = ('is_active',)
    search_fields = ('id', 'first_name', 'last_name', 'username')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ('is_customer','is_business','is_regional_manager','is_active')
    fieldsets = ()


# Customer Admin
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'get_name', 'get_email', 'get_status')
    list_display_links = ('customer_id', 'get_name', 'get_email')
    readonly_fields = ['customer_id']


    def get_name(self, obj):
        return obj.user.name
    get_name.short_description = 'Name'
    get_name.admin_order_field = 'user__name'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'
    get_email.admin_order_field = 'user__email'

    def get_status(self, obj):
        return obj.user.is_active
    get_status.short_description = 'Is Active'
    get_status.admin_order_field = 'user__status'


# Business Admin
class BusinessAdmin(admin.ModelAdmin):
    list_display_links = ('business_id', 'get_name', 'domain_name', 'get_email')
    list_display = ('business_id', 'get_name', 'domain_name', 'get_email', 'get_status')
    readonly_fields = ['business_id']

    def get_name(self, obj):
        return obj.user.name
    get_name.short_description = 'Name'
    get_name.admin_order_field = 'user__name'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'
    get_email.admin_order_field = 'user__email'

    def get_status(self, obj):
        return obj.user.is_active
    get_status.short_description = 'Is Active'
    get_status.admin_order_field = 'user__status'

# Regional Manager Admin
class RegionalManagerAdmin(admin.ModelAdmin):
    list_display_links = ('regional_manager_id', 'get_name', 'get_email')
    list_display = ('regional_manager_id', 'get_name', 'get_email', 'is_verification_email_sent', 'is_account_verified', 'get_status')
    readonly_fields = ['regional_manager_id']

    def get_name(self, obj):
        return obj.user.name
    get_name.short_description = 'Name'
    get_name.admin_order_field = 'user__name'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'
    get_email.admin_order_field = 'user__email'

    def get_status(self, obj):
        return obj.user.is_active
    get_status.short_description = 'Is Active'
    get_status.admin_order_field = 'user__status'


# State Admin
class StateAdmin(admin.ModelAdmin):
    list_display = ('state_name', 'country')
    list_display_links = ('state_name',)
    list_filter = ('country',)
    search_fields = ('state_name',)


# Register the models
admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Country)
admin.site.register(State, StateAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(RegionalManager, RegionalManagerAdmin)
