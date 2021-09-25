from products.models import Testimonial
from django import forms


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['testimonial',]
        widgets = {
          'testimonial': forms.Textarea(attrs={'rows':4, 'cols':15, 'required':'required'}),
        }