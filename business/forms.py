from django import forms
from accounts.models import User, Business
from .models import PaymentSetting


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
