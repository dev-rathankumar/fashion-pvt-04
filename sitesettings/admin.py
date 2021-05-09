from django.contrib import admin
from .models import Header, Footer, ContactPage, Homepage, BannerImage, StoreFeature, ParallaxBackground
import admin_thumbnails


class BannerImageInline(admin.TabularInline):
    model = BannerImage
    list_display = ('homepage', 'title')
    extra = 1


class StoreFeatureInline(admin.TabularInline):
    model = StoreFeature
    list_display = ('homepage', 'title', 'sub_title')
    extra = 1
    max_num = 4


class ParallaxBackgroundInline(admin.TabularInline):
    model = ParallaxBackground
    list_display = ('homepage', 'title')
    extra = 1
    max_num = 1


class HomepageAdmin(admin.ModelAdmin):
    list_display = ('business',)
    inlines = [BannerImageInline, StoreFeatureInline, ParallaxBackgroundInline]


class HeaderAdmin(admin.ModelAdmin):
    list_display = ['business', 'site_title']

class ParallaxBackgroundAdmin(admin.ModelAdmin):
    list_display = ['homepage', 'title', 'button_name']
    max_num = 1


class ContactPageAdmin(admin.ModelAdmin):
    list_display = ['business', 'address_line_1', 'city', 'country', 'state', 'modified_date']

    # if there's already an entry, do not allow adding
    def has_add_permission(self, request):
        count = ContactPage.objects.all().count()
        if count == 0:
          return True
        return False

admin.site.register(Header, HeaderAdmin)
admin.site.register(Footer)
admin.site.register(ContactPage, ContactPageAdmin)
admin.site.register(Homepage, HomepageAdmin)
admin.site.register(BannerImage)
admin.site.register(ParallaxBackground, ParallaxBackgroundAdmin)
admin.site.register(StoreFeature)
