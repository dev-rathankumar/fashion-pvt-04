from django.shortcuts import render, redirect
from accounts.models import User, RegionalManager
from django.http import HttpResponse
import json
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        try:
            if not user.is_regional_manager:
                messages.error(request, "This is not a regional manager's account")
                return redirect('rm_login')
        except AttributeError:
            messages.error(request, "Invalid login credentials")
            return redirect('rm_login')

        if user is None:
            User = get_user_model()
            user_queryset = User.objects.all().filter(email__iexact=username)
            if user_queryset:
                username = user_queryset[0].username
                user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('rm_dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('rm_login')
    return render(request, 'regional_managers/login.html')

@login_required(login_url = 'rm_login')
def dashboard(request):
    return render(request, 'regional_managers/dashboard.html')

@login_required(login_url = 'rm_login')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.warning(request, 'You are now logged out')
        return redirect('rm_login')
    return redirect('rm_login')


def forgotPassword(request):
    """Send password reset email to regional manager"""
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)
            if user.is_regional_manager == True:
                current_site = get_current_site(request)
                # return HttpResponse(current_site)
                mail_subject = 'Reset Your Password'
                message = render_to_string('regional_managers/reset_password_email.html', {
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
                return redirect('rm_login')
            else:
                messages.warning(request, "This is not a Regional Manager's account")
                return redirect('rm_forgotPassword')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('rm_forgotPassword')
    else:
        return render(request, 'regional_managers/forgotPassword.html')


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
        return redirect('rm_resetForgotPassword')
    else:
        messages.error(request, 'This link has been expired')
        return redirect('rm_forgotPassword')


def rm_resetPassword(request):
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
            return redirect('rm_login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('rm_resetForgotPassword')
    else:
        return render(request, 'regional_managers/resetPassword.html')


@login_required(login_url = 'rm_login')
def rm_profile(request):
    current_user = request.user
    rm = RegionalManager.objects.get(user__id=current_user.id)

    context = {
        'rm': rm,
    }
    return render(request, 'regional_managers/profile.html', context)


@login_required(login_url = 'rm_login')
def rm_changePassword(request):
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
    return render(request, 'regional_managers/changePassword.html')
