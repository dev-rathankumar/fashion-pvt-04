from django import forms
from ckeditor.widgets import CKEditorWidget
from django.forms import inlineformset_factory
from .models import Header, BannerImage, StoreFeature, ParallaxBackground



class HeaderForm(forms.ModelForm):
    # site_logo = forms.ImageField(label=('Logo'),required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
    site_logo = forms.ImageField(label=('Logo'), required=True, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput(attrs={
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


class BannerImageForm(forms.ModelForm):
    banner_image = forms.ImageField(label=('Banner Image'), required=True, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput(attrs={
        "type": "file",
        "data-show-preview": "false"
    }))
    class Meta:
        model = BannerImage
        fields = ['banner_image', 'title', 'sub_title', 'button_name', 'button_link', 'button_color', 'content_align']

    # Give same CSS class to all the fields
    def __init__(self, *args, **kwargs):
        super(BannerImageForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            if myField == 'banner_image':
                self.fields[myField].widget.attrs['class'] = 'form-control file'
            else:
                self.fields[myField].widget.attrs['class'] = 'form-control'


class StoreFeatureForm(forms.ModelForm):
    icon = forms.ImageField(label=('Feature Icon'), required=True, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput(attrs={
        "type": "file",
        "data-show-preview": "false"
    }))
    class Meta:
        model = StoreFeature
        fields = ['icon', 'title', 'sub_title']

    # Give same CSS class to all the fields
    def __init__(self, *args, **kwargs):
        super(StoreFeatureForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            if myField == 'icon':
                self.fields[myField].widget.attrs['class'] = 'form-control file'
            else:
                self.fields[myField].widget.attrs['class'] = 'form-control'


class ParallaxBackgroundForm(forms.ModelForm):
    parallax_image = forms.ImageField(label=('Background Image'), required=True, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput(attrs={
        "type": "file",
        "data-show-preview": "false"
    }))
    class Meta:
        model = ParallaxBackground
        fields = ['parallax_image', 'title', 'description', 'button_name', 'button_link', 'button_color', 'content_align']

    # Give same CSS class to all the fields
    def __init__(self, *args, **kwargs):
        super(ParallaxBackgroundForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            if myField == 'parallax_image':
                self.fields[myField].widget.attrs['class'] = 'form-control file'
            else:
                self.fields[myField].widget.attrs['class'] = 'form-control'
