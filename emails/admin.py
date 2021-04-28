from django.contrib import admin
from .models import Email
from accounts.models import User


class EmailAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
         context['adminform'].form.fields['to_address'].queryset = User.objects.filter(is_customer=True, is_active=True)
         return super(EmailAdmin, self).render_change_form(request, context, *args, **kwargs)


admin.site.register(Email, EmailAdmin)
