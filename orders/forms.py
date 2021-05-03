from django import forms
from accounts.models import User, Customer


class BillingUserInfoForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
    }), label="Email")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']


class BillingCustomerInfoForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
    }), label="Email")

    class Meta:
        model = Customer
        fields = ['address_line_1', 'address_line_2', 'city', 'pin_code', 'country', 'state']
