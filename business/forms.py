from django import forms
from accounts.models import User, Business
from .models import PaymentSetting
from products.models import Product, ProductGallery, Variants
from ckeditor.widgets import CKEditorWidget
from django.forms import inlineformset_factory


class UserForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
    }), label="Email")
    profile_picture = forms.ImageField(required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput(attrs={
        "class": "file",
        "type": "file",
        # "data-browse-on-zone-click": "true",
        "data-show-preview": "false"
    }))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'gender', 'profile_picture']

    # Give same CSS class to all the fields
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
          self.fields[myField].widget.attrs['class'] = 'form-control'


class BusinessForm(forms.ModelForm):
    is_editing = forms.BooleanField(widget=forms.HiddenInput(attrs={
        "type": "hidden",
        'value': 'True',
    }), initial=1)
    is_editing = forms.BooleanField(required=False,initial=True)
    class Meta:
        model = Business
        fields = ['company_name', 'country', 'state', 'city', 'pin_code', 'address_line_1', 'address_line_2']
        exclude = ('user',)

        # Give same CSS class to all the fields
    def __init__(self, *args, **kwargs):
        super(BusinessForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
          self.fields[myField].widget.attrs['class'] = 'form-control'


class PaymentSettingForm(forms.ModelForm):
    CHOICES = (('PayPal', 'PayPal'),('Bank Account', 'Bank Account'),)
    payment_method = forms.CharField(widget=forms.Select(choices=CHOICES))
    class Meta:
        model = PaymentSetting
        fields = ['payment_method', 'paypal_address', 'bank_name', 'bank_account_name', 'bank_account_number', 'bank_code']

        # Give same CSS class to all the fields
    def __init__(self, *args, **kwargs):
        super(PaymentSettingForm, self).__init__(*args, **kwargs)
        self.fields['payment_method'].widget.attrs['onchange'] = 'showDiv(this)'
        for myField in self.fields:
          self.fields[myField].widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    image = forms.ImageField(label=('Product Image 01'), required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput(attrs={
        "type": "file",
        # "data-browse-on-zone-click": "true",
        "data-show-preview": "false"
    }))
    image_2 = forms.ImageField(label=('Product Image 02'), required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput(attrs={
        "type": "file",
        # "data-browse-on-zone-click": "true",
        "data-show-preview": "false"
    }))
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'full_specification', 'price', 'variant', 'image', 'image_2', 'stock', 'category', 'is_popular']

    # Give same CSS class to all the fields
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            if myField == 'is_popular':
                self.fields[myField].widget.attrs['class'] = 'custom-chckbox-is_popular'
            elif myField == 'image' or myField == 'image_2':
                self.fields[myField].widget.attrs['class'] = 'form-control file'
            else:
                self.fields[myField].widget.attrs['class'] = 'form-control'




class ProductGalleryForm(forms.ModelForm):
    image = forms.ImageField(label=('Product Gallery Image'), required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput(attrs={
        "type": "file",
        "class": "file",
        # "data-browse-on-zone-click": "true",
        "data-show-preview": "false"
    }))
    class Meta:
        model = ProductGallery
        fields = ('image',)
        exclude = ()


class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = Variants
        fields = ('title', 'color', 'size', 'image_id', 'quantity', 'price')
        exclude = ()

    # Give same CSS class to all the fields
    def __init__(self, *args, **kwargs):
        super(ProductVariantForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            if myField == 'image_id':
                self.fields[myField].widget.attrs['class'] = 'form-control image_id'
                # self.fields[myField].widget.attrs['onfocus'] = 'image_idFocus(this)'
            else:
                self.fields[myField].widget.attrs['class'] = 'form-control'
