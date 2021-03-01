from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from accounts.models import User
from accounts.models import Business
from django.http import HttpResponse
from .forms import PaymentSettingForm
from .models import PaymentSetting

from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from datetime import date, datetime
import time

import json
from django.contrib import messages

from .forms import UserForm, BusinessForm, ProductForm, ProductGalleryForm, ProductVariantForm

from products.models import Product, ProductGallery, Variants
from django.forms import inlineformset_factory
from django import forms
from django.template.defaultfilters import slugify


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        try:
            if not user.is_business:
                messages.error(request, "This is not a business account")
                return redirect('biz_login')
        except AttributeError:
            messages.error(request, "Invalid login credentials")
            return redirect('biz_login')

        if user is not None:
            # Check for the expiry date
            biz = Business.objects.get(user__id=user.id)
            get_exp_date = biz.account_expiry_date
            exp_date = datetime.strptime(str(get_exp_date), '%Y-%m-%d')
            get_today = date.today()
            today = datetime.strptime(str(get_today), '%Y-%m-%d')
            if today > exp_date:
                messages.error(request, "Your account is expired.")
                return redirect('biz_login')
            else:
                auth.login(request, user)
                messages.success(request, 'You are now logged in.')
                return redirect('biz_dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('biz_login')
    return render(request, 'business/login.html')


@login_required(login_url = 'biz_login')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('biz_login')
    return redirect('biz_login')

@login_required(login_url = 'biz_login')
def dashboard(request):
    return render(request, 'business/dashboard.html')

@login_required(login_url = 'biz_login')
def biz_profile(request):
    current_user = request.user
    biz = Business.objects.get(user__id=current_user.id)

    context = {
        'biz': biz,
    }
    return render(request, 'business/profile.html', context)

@login_required(login_url = 'biz_login')
def biz_changePassword(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        user = User.objects.get(username__exact=request.user.username)

        if password == confirm_password:
            success = user.check_password(request.POST['current_password'])
            if success:
                user.set_password(password)
                user.save()
                auth.logout(request)
                messages.success(request, 'Password updated successfully. Please login again.')
                return HttpResponse('success')
            else:
                return HttpResponse('Please enter valid current password')
        else:
            return HttpResponse('Passwords do not match!')
    return render(request, 'business/changePassword.html')


def forgotPassword(request):
    """Send password reset email to Business"""
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)
            if user.is_business == True:
                current_site = get_current_site(request)
                # return HttpResponse(current_site)
                mail_subject = 'Reset Your Password'
                message = render_to_string('business/reset_password_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                to_email = email
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                messages.warning(request, 'Password reset link has been sent to your email address.')
                return redirect('biz_login')
            else:
                messages.warning(request, "This is not a Business account")
                return redirect('biz_forgotPassword')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('biz_forgotPassword')
    else:
        return render(request, 'business/forgotPassword.html')

def resetpassword_validate(request, uidb64, token):
    """Resetting password request validation"""
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('biz_resetForgotPassword')
    else:
        messages.error(request, 'This link has been expired')
        return redirect('biz_forgotPassword')

def biz_resetPassword(request):
    """Reset password"""
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = User.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('biz_login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('biz_resetForgotPassword')
    else:
        return render(request, 'business/resetPassword.html')


def editProfile(request, pk=None):
    user = get_object_or_404(User, pk=pk)
    business = get_object_or_404(Business, pk=pk)
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES, instance=user, prefix="user")
        business_form = BusinessForm(request.POST, prefix="business")
        if user_form.is_valid() and business_form.is_valid():
            user = user_form.save()
            business_form.cleaned_data["user"] = user
            current_user = request.user
            biz = Business.objects.get(user=current_user)
            business = business_form.save(commit=False)
            business.user = request.user
            business.is_editing = True
            business.is_verification_email_sent = True
            business.is_account_verified = True
            business.business_id = biz.business_id
            business.domain_name = biz.domain_name
            business.account_activation_date = biz.account_activation_date
            business.account_expiry_date = biz.account_expiry_date
            business.regional_manager = biz.regional_manager
            business.created_date = biz.created_date
            business_form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('/business/editProfile/'+str(pk))
        else:
            print('user form', user_form.errors)
            print('rm form', business_form.errors)
    else:
        user_form = UserForm(instance=user, prefix="user")
        business_form = BusinessForm(instance=business, prefix="business")
    context = {
        'user_form': user_form,
        'business_form': business_form,
        'user': user,
        'business': business,
    }
    return render(request, 'business/editProfile.html', context)


def paymentSettings(request, pk=None):
    user = get_object_or_404(User, pk=pk)
    pay_setting = get_object_or_404(PaymentSetting, user=user)
    if request.method == 'POST':
        form = PaymentSettingForm(request.POST, instance=pay_setting)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your payment settings are saved successfully.')
            return redirect('/business/paymentSettings/'+str(pk))
    else:
        form = PaymentSettingForm(instance=pay_setting)

    context = {
        'form': form,
    }
    return render(request, 'business/paymentSettings.html', context)


def allProducts(request):
    business = get_object_or_404(Business, pk=request.user.id)
    products = Product.objects.filter(business=business)

    context = {
        'products': products,
    }
    return render(request, 'business/allProducts.html', context)


def editProduct(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        basicInfo_form = ProductForm(request.POST, request.FILES, instance=product)
        if basicInfo_form.is_valid():
            basicInfo_form.save()
            return redirect('/business/products/editProduct/'+str(pk)+'/editGallery/')
        else:
            print(basicInfo_form.errors)

    else:
        basicInfo_form = ProductForm(instance=product)
    context = {
        'basicInfo_form': basicInfo_form,
        'product': product,
    }
    return render(request, 'business/editProduct.html', context)


def editGallery(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    ProductGalleryFormSet = inlineformset_factory(Product, ProductGallery, form=ProductGalleryForm, extra=1)

    if request.method == 'POST':
        add_another = request.POST['add_another']
        formset = ProductGalleryFormSet(request.POST, request.FILES, instance=product)
        if formset.is_valid():
            formset.save()
            if add_another == 'true':
                return redirect('/business/products/editProduct/'+str(pk)+'/editGallery/')
            else:
                return redirect('/business/products/editProduct/'+str(pk)+'/editVariants/')
        else:
            return HttpResponse(formset.errors)
    else:
        formset = ProductGalleryFormSet(instance=product)
    context = {
        'product' : product,
        'formset': formset,
    }
    return render(request, 'business/editGallery.html', context)


def editVariants(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    ProductVariantFormSet = inlineformset_factory(Product, Variants, form=ProductVariantForm, extra=1)

    if request.method == 'POST':
        add_another = request.POST['add_another']
        formset = ProductVariantFormSet(request.POST, instance=product)
        if formset.is_valid():
            formset.save()
            if add_another == 'true':
                return redirect('/business/products/editProduct/'+str(pk)+'/editVariants/')
            else:
                messages.success(request, 'Product has been uploaded successfully.')
                return redirect('allProducts')
        else:
            return HttpResponse(formset.errors)
    else:
        formset = ProductVariantFormSet(instance=product)
        gallery = ProductGallery.objects.filter(product=product)

    context = {
        'product' : product,
        'formset': formset,
        'gallery': gallery,
    }
    return render(request, 'business/editVariants.html', context)

def addProduct(request):
    if request.method == 'POST':
        basicInfo_form = ProductForm(request.POST, request.FILES)
        if basicInfo_form.is_valid():
            current_user = request.user
            business_name = Business.objects.get(user=current_user)
            product_name = basicInfo_form.cleaned_data['product_name']
            product = basicInfo_form.save(commit=False)
            product.business = business_name
            product.slug = slugify(product_name)
            basicInfo_form.save()
            return redirect('addProduct')
        else:
            print(basicInfo_form.errors)
    else:
        basicInfo_form = ProductForm()
    context = {
        'basicInfo_form': basicInfo_form,
    }

    return render(request, 'business/addProduct.html', context)
