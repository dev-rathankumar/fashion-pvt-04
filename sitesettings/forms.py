from django import forms
from ckeditor.widgets import CKEditorWidget
from django.forms import inlineformset_factory
from .models import Header, BannerImage, StoreFeature, ParallaxBackground, ContactPage, Footer, SocialMediaLink, AboutPage, Policy, TermsAndCondition, Topbar



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
        fields = ['icon', 'title', 'sub_title','feature_url']

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


class ContactPageForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
    }), label="Email")

    class Meta:
        model = ContactPage
        fields = ['address_line_1', 'address_line_2', 'city', 'pin_code', 'country', 'state', 'phone_number', 'email', 'embed_google_map']

    # Give same CSS class to all the fields
    def __init__(self, *args, **kwargs):
        super(ContactPageForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'


class AboutPageForm(forms.ModelForm):
    cover_image = forms.ImageField(label=('Cover Image'), required=True, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput(attrs={
        "type": "file",
        "data-show-preview": "false"
    }))

    class Meta:
        model = AboutPage
        fields = ['heading', 'sub_heading', 'description', 'cover_image']

    # Give same CSS class to all the fields
    def __init__(self, *args, **kwargs):
        super(AboutPageForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            if myField == 'cover_image':
                self.fields[myField].widget.attrs['class'] = 'form-control file'
            else:
                self.fields[myField].widget.attrs['class'] = 'form-control'


class FooterForm(forms.ModelForm):
    class Meta:
        model = Footer
        fields = ['footer_text','footer_align']

    # Give same CSS class to all the fields
    def __init__(self, *args, **kwargs):
        super(FooterForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'



class SocialMediaLinkForm(forms.ModelForm):
    class Meta:
        model = SocialMediaLink
        fields = ['social_media_name', 'icon', 'link']

    # Give same CSS class to all the fields
    def __init__(self, *args, **kwargs):
        super(SocialMediaLinkForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'


class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ['heading', 'content']

    def __init__(self, *args, **kwargs):
        super(PolicyForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'


class TermsAndConditionForm(forms.ModelForm):
    class Meta:
        model = TermsAndCondition
        fields = ['heading', 'content']

    def __init__(self, *args, **kwargs):
        super(TermsAndConditionForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'


class TopbarForm(forms.ModelForm):
    class Meta:
        model = Topbar
        fields = ['topbar_text']

    # Give same CSS class to all the fields
    def __init__(self, *args, **kwargs):
        super(TopbarForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'
