from django import forms
from ckeditor.widgets import CKEditorWidget
from django.forms import inlineformset_factory
from .models import Email
from accounts.models import User


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['to_address', 'subject', 'email_body', 'is_sent']

    # Give same CSS class to all the fields
    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.fields['to_address'].queryset = User.objects.filter(is_customer=True, is_active=True)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'
