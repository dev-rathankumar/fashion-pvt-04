from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from .models import User, RegionalManager, Business
from contacts.models import Inquiry
from products.models import Product

# Send account verification email
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import UserForm

from django.http import HttpResponse
from urllib.parse import urlparse

# Create your views here.
def userRegister(request):
    """User Registration"""
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']


        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('userRegister')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('userRegister')
                else:
                    user = User.objects.create_user(first_name=first_name,
                    last_name=last_name, username=username, email=email, password=password)
                    user.is_customer = True
                    user.profile_picture="default/default-user.png"
                    user.save()
                    # Send account verification email
                    current_site = get_current_site(request)
                    mail_subject = 'Activate your account.'
                    message = render_to_string('accounts/acc_active_email.html', {
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
                    messages.warning(request, 'Please confirm your email address to complete the registration')
                    return redirect('userLogin')
        else:
            messages.error(request, 'Password do not match')
            return redirect('userRegister')
    else:
        return render(request, 'accounts/userRegister.html')


def activate(request, uidb64, token):
    """Activating Users"""
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('userLogin')
    else:
        messages.error(request, 'Activation link is invalid')
        return redirect('userRegister')


def userLogin(request):
    """User Login"""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            try:
                if user.is_business:
                    auth.login(request, user)
                    messages.success(request, "You are now logged in!")
                    return redirect('biz_dashboard')
                elif user.is_regional_manager:
                    auth.login(request, user)
                    messages.success(request, "You are now logged in!")
                    return redirect('rm_dashboard')
                elif user.is_superadmin:
                    auth.login(request, user)
                    messages.success(request, "You are now logged in!")
                    return redirect('userDashboard')
                else:
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in.')
                    return redirect('userDashboard')
            except:
                pass
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('userLogin')
    return render(request, 'accounts/userLogin.html')


@login_required(login_url='/userLogin')
def userDashboard(request):
    return render(request, 'accounts/userDashboard.html')

@login_required(login_url='/userLogin')
def editUser(request, pk=None):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully saved.')
            return redirect('/userDashboard/user/edit/'+str(pk))
    else:
        form = UserForm(instance=user)
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'accounts/editUser.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out.')
        return redirect('userLogin')
    return redirect('home')


def forgotPassword(request):
    """Send password reset email"""
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('accounts/reset_password_email.html', {
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
            return redirect('userLogin')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('forgotPassword')
    else:
        return render(request, 'accounts/forgotPassword.html')


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
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has been expired')
        return redirect('userLogin')


def resetPassword(request):
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
            return redirect('userLogin')
        else:
            messages.error(request, 'Password do not match')
            return redirect('resetPassword')
    else:
        return render(request, 'accounts/resetPassword.html')


# Regional Manager Activation Validation
def rm_password_reset_validate(request, uidb64, token):
    """Regional Manager Resetting password request validation"""
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('rm_password_reset')
    else:
        messages.error(request, 'This link has been expired')
        return redirect('home')

# Regional Manager Activation
def rm_password_reset(request):
    """Reset password"""
    if request.method == 'POST':
        rm_id = request.session['uid']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = User.objects.get(pk=rm_id)
            regional_manager = RegionalManager.objects.get(user=user)
            user.set_password(password)
            user.is_regional_manager = True
            user.is_active = True
            regional_manager.is_account_verified = True
            user.save()
            regional_manager.save()
            mail_subject = 'Your Account is Activated'
            message = 'Congratulations! Your account has been activated.'
            to_email = user.email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request, 'Congratulations! Your business account has been activated.')
            return redirect('rm_login')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('rm_password_reset')
    else:
        return render(request, 'accounts/rm_password_reset.html')


# Business Activation Validation
def biz_password_reset_validate(request, uidb64, token):
    """Business Resetting password request validation"""
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('biz_password_reset')
    else:
        messages.error(request, 'This link has been expired')
        return redirect('biz_login')

# Business Activation
def biz_password_reset(request):
    """Reset password"""
    if request.method == 'POST':
        biz_id = request.session['uid']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = User.objects.get(pk=biz_id)
            business = Business.objects.get(user=user)
            user.set_password(password)
            user.is_business = True
            user.is_active = True
            business.is_account_verified = True
            user.save()
            business.save()
            mail_subject = 'Your Business Account is Activated'
            message = 'Congratulations! Your business account has been activated.'
            to_email = user.email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request, 'Congratulations! Your account has been activated.')
            return redirect('biz_login')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('biz_password_reset')
    else:
        return render(request, 'accounts/biz_password_reset.html')


@login_required(login_url='/userLogin')
def userInquiry(request):
    user_inquiry = Inquiry.objects.order_by('-create_date').filter(user_id=request.user.id)
    
    context = {
            'inquiries': user_inquiry,
        }
    return render(request, 'accounts/inquiries.html', context)
