from django.forms import ModelForm
from .models import TestRathan, SiteSetting
from django import forms


class TestRathanForm(ModelForm):
    class Meta:
        model = TestRathan
        fields = '__all__'
        exclude = ['business_test']
        # widgets = {'business_test': forms.HiddenInput()}


class SiteSettingForm(ModelForm):
    class Meta:
        model = SiteSetting
        fields = '__all__'
        exclude = ['business']
