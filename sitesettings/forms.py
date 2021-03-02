from django import forms
from ckeditor.widgets import CKEditorWidget
from django.forms import inlineformset_factory
from .models import Header


class HeaderForm(forms.ModelForm):
    # site_logo = forms.ImageField(label=('Logo'),required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
    site_logo = forms.ImageField(label=('Logo'), required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput(attrs={
        "type": "file",
        # "data-browse-on-zone-click": "true",
        "data-show-preview": "false"
    }))
    favicon = forms.ImageField(label=('Favicon'), required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput(attrs={
        "type": "file",
        # "data-browse-on-zone-click": "true",
        "data-show-preview": "false"
    }))
    class Meta:
        model = Header
        fields = ['site_title', 'site_logo', 'favicon']

    # Give same CSS class to all the fields
    def __init__(self, *args, **kwargs):
        super(HeaderForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
          self.fields[myField].widget.attrs['class'] = 'form-control file'
