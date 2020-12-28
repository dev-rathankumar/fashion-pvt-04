from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from accounts.models import User
from .models import SiteSetting, TestRathan
from .forms import TestRathanForm, SiteSettingForm
from django.http import HttpResponse

import json
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        # return HttpResponse(user)
        # exit()
        try:
            if not user.is_business:
                return HttpResponse('not business')
        except AttributeError:
            return HttpResponse('invalid request')

        if user is None:
            User = get_user_model()
            user_queryset = User.objects.all().filter(email__iexact=username)
            if user_queryset:
                username = user_queryset[0].username
                user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'business/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')

@login_required(login_url = 'login')
def dashboard(request):
    return render(request, 'business/dashboard.html')

# Site settings
@login_required(login_url = 'login')
def site_settings(request):
    form = SiteSettingForm()
    if request.method == 'POST':
        user_id = request.user.id
        instance = get_object_or_404(SiteSetting, business=user_id)
        form = SiteSettingForm(request.POST or None, request.FILES, instance=instance)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.business = request.user.business
            biz.save()
            return HttpResponse('Record saved.')
        else:
            errors = form.errors
            return HttpResponse(json.dumps(errors))

    context = {
        'form': form,
    }
    return render(request, 'business/site_settings.html', context)



def site_settings_create(request):
    form = TestRathanForm()

    if request.method == 'POST':
        instance = get_object_or_404(TestRathan, business_test='4')
        form = TestRathanForm(request.POST or None, instance=instance)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.business_test = request.user.business
            biz.save()
            return HttpResponse('Record saved.')
        else:
            errors = form.errors
            return HttpResponse(json.dumps(errors))

    context = {
        'form': form,
    }
    return render(request, 'business/site_settings.html', context)
