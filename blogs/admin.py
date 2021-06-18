from django.contrib import admin
from .models import Blog, Category
from mptt.admin import DraggableMPTTAdmin



class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "category_name"
    list_display = ('tree_actions', 'indented_title',
                    'related_blogs_count', 'related_blogs_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('category_name',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative blog count
        qs = Category.objects.add_related_count(
                qs,
                Blog,
                'category',
                'blogs_cumulative_count',
                cumulative=True)

        # Add non cumulative blog count
        qs = Category.objects.add_related_count(qs,
                 Blog,
                 'category',
                 'blogs_count',
                 cumulative=False)
        return qs

    def related_blogs_count(self, instance):
        return instance.blogs_count
    related_blogs_count.short_description = 'Related blogs (for this specific category)'

    def related_blogs_cumulative_count(self, instance):
        return instance.blogs_cumulative_count
    related_blogs_cumulative_count.short_description = 'Related blogs (in tree)'

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
