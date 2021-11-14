from products.models import Testimonial
from django import forms
from modeltranslation.forms import TranslationModelForm


class TestimonialForm(TranslationModelForm):
    class Meta:
        model = Testimonial
        fields = ['testimonial',]
        widgets = {
          'testimonial': forms.Textarea(attrs={'rows':4, 'cols':15, 'required':'required'}),
        }