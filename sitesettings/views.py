from django.shortcuts import render, get_object_or_404, redirect
from .models import Header
from .forms import HeaderForm
from django.contrib import messages
from django.http import HttpResponse
from accounts.models import Business


def header(request):
    current_user = request.user
    try:
        header = Header.objects.get(business=current_user.id)
        return redirect('headerEdit', header.id)
    except Header.DoesNotExist:
        return redirect('headerAdd')


def headerEdit(request, pk=None):
    header = get_object_or_404(Header, pk=pk)
    if request.method == 'POST':
        form = HeaderForm(request.POST, request.FILES, instance=header)
        if form.is_valid():
            form.save()
            messages.success(request, 'Settings applied successfully.')
            return redirect('header')
    else:
        form = HeaderForm(instance=header)
    context = {
        'form': form,
        'header': header,
    }
    return render(request, 'business/sitesettings/headerEdit.html', context)


def headerAdd(request):
    if request.method == 'POST':
        form = HeaderForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            header = form.save(commit=False)
            business_name = Business.objects.get(user=current_user)
            header.business = business_name
            form.save()
            messages.success(request, 'Settings applied successfully.')
            return redirect('headerEdit', header.id)

    else:
        form = HeaderForm()
    context = {
        'form': form,
    }
    return render(request, 'business/sitesettings/headerAdd.html', context)
