from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from accounts.models import User
from accounts.models import Business
from django.http import HttpResponse

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
            return HttpResponse('Password do not match!')
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
