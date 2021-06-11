from django.core.mail import message
from products.models import ReviewRating
from django.shortcuts import render, get_object_or_404, redirect
from .models import Header, Homepage, BannerImage, StoreFeature, ParallaxBackground, ContactPage, Footer, SocialMediaLink, AboutPage, Policy, TermsAndCondition, Topbar
from .forms import HeaderForm, BannerImageForm, StoreFeatureForm, ParallaxBackgroundForm, ContactPageForm, FooterForm, SocialMediaLinkForm, AboutPageForm, PolicyForm, TermsAndConditionForm, TopbarForm
from django.contrib import messages
from django.http import HttpResponse
from accounts.models import Business
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from business.views import business_required


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def header(request):
    current_user = request.user
    try:
        header = Header.objects.get(business=current_user.id)
        return redirect('headerEdit', header.id)
    except Header.DoesNotExist:
        return redirect('headerAdd')


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
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


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
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


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def banners(request):
    try:
        business = Business.objects.get(user=request.user)
        homepage = Homepage.objects.get(business=business)
    except:
        pass
    banners = BannerImage.objects.filter(homepage=homepage)
    context = {
        'banners': banners,
    }
    return render(request, 'business/sitesettings/banners.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def addBanner(request):
    if request.method == 'POST':
        form = BannerImageForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            banner = form.save(commit=False)
            business_name = Business.objects.get(user=current_user)

            homepage = Homepage.objects.get(business=business_name)
            banner.homepage = homepage
            form.save()
            messages.success(request, 'Banner saved successfully.')
            return redirect('banners')
    else:
        form = BannerImageForm()
    context = {
        'form':form,
    }
    return render(request, 'business/sitesettings/addBanner.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def editBanner(request, pk=None):
    banner = get_object_or_404(BannerImage, pk=pk)
    if request.method == 'POST':
        form = BannerImageForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            messages.success(request, 'Banner updated successfully.')
            return redirect('banners')
    else:
        form = BannerImageForm(instance=banner)
    context = {
        'form': form,
        'banner': banner,
    }
    return render(request, 'business/sitesettings/editBanner.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def deleteBanner(request, pk=None):
    banner = get_object_or_404(BannerImage, pk=pk)
    banner.delete()
    messages.success(request, 'Banner has been deleted.')
    return redirect('banners')


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def store_features(request):
    try:
        business = Business.objects.get(user=request.user)
        homepage = Homepage.objects.get(business=business)
    except:
        pass
    store_features = StoreFeature.objects.filter(homepage=homepage)
    features_count = store_features.count()
    context = {
        'store_features': store_features,
        'features_count': features_count,
    }
    return render(request, 'business/sitesettings/store_features.html', context)


def addFeature(request):
    homepage = Homepage.objects.get(business__user=request.user)
    store_features = StoreFeature.objects.filter(homepage=homepage)
    features_count = store_features.count()
    if features_count >= 4:
        messages.warning(request, 'Only 4 store features allowed!')
        return redirect('store_features')
    else:
        form = StoreFeatureForm(request.POST, request.FILES)
        if request.method == 'POST':
            if form.is_valid():
                current_user = request.user
                feature = form.save(commit=False)
                business_name = Business.objects.get(user=current_user)

                homepage = Homepage.objects.get(business=business_name)
                feature.homepage = homepage
                form.save()
                messages.success(request, 'Feature saved successfully.')
                return redirect('store_features')
        else:
            form = StoreFeatureForm()
    context = {
        'form': form,
    }
    return render(request, 'business/sitesettings/addStoreFeature.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def editFeature(request, pk=None):
    feature = get_object_or_404(StoreFeature, pk=pk)
    if request.method == 'POST':
        form = StoreFeatureForm(request.POST, request.FILES, instance=feature)
        if form.is_valid():
            form.save()
            messages.success(request, 'Feature updated successfully.')
            return redirect('store_features')
    else:
        form = StoreFeatureForm(instance=feature)
    context = {
        'form': form,
        'feature': feature,
    }
    return render(request, 'business/sitesettings/editStoreFeature.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def deleteFeature(request, pk=None):
    feature = get_object_or_404(StoreFeature, pk=pk)
    feature.delete()
    messages.success(request, 'Feature has been deleted.')
    return redirect('store_features')


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def homepage_background(request):
    homepage = Homepage.objects.get(business__user=request.user)
    background = get_object_or_404(ParallaxBackground, homepage=homepage)
    if request.method == "POST":
        form = ParallaxBackgroundForm(request.POST, request.FILES, instance=background)
        form.save()
        messages.success(request, 'Background Image updated successfully.')
        return redirect('homepage_background')
    else:
        form = ParallaxBackgroundForm(instance=background)
    context = {
        'form': form,
        'background': background,
    }
    return render(request, 'business/sitesettings/homepage_background.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def aboutUs(request):
    business = Business.objects.get(user=request.user)
    about_page = get_object_or_404(AboutPage, business=business)
    if request.method == 'POST':
        form = AboutPageForm(request.POST, request.FILES, instance=about_page)
        if form.is_valid():
            about = form.save(commit=False)
            about.business = business
            form.save()
            messages.success(request, 'Settings saved successfully')
            return redirect('aboutUs')
        else:
            print(form.errors)
    else:
        form = AboutPageForm(instance=about_page)
    context = {
        'form': form,
        'about_page': about_page,
    }
    return render(request, 'business/sitesettings/aboutUs.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def contactUs(request):
    business = Business.objects.get(user=request.user)
    contact_page = get_object_or_404(ContactPage, business=business)
    if request.method == 'POST':
        form = ContactPageForm(request.POST, instance=contact_page)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.business = business
            form.save()
            messages.success(request, 'Settings saved successfully')
            return redirect('contactUs')
    else:
        form = ContactPageForm(instance=contact_page)
    context = {
        'form': form,
    }
    return render(request, 'business/sitesettings/contactUs.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def footerEdit(request):
    business = Business.objects.get(user=request.user)
    footer = get_object_or_404(Footer, business=business)

    if request.method == 'POST':
        form = FooterForm(request.POST, instance=footer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Footer Copyright updated successfully')
            return redirect('footerEdit')
    else:
        form = FooterForm(instance=footer)
    context = {
        'form': form,
        'footer': footer,
    }
    return render(request, 'business/sitesettings/footerEdit.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def topbarEdit(request):
    business = Business.objects.get(user=request.user)
    # try:
    #     checkTopbar = Topbar.objects.get(business=business, is_enabled=True)
    # except:
    #     checkTopbar = None
    topbar = get_object_or_404(Topbar, business=business)

    if request.method == 'POST':
        form = TopbarForm(request.POST, instance=topbar)
        if form.is_valid():
            form.save()
            messages.success(request, 'Topbar updated successfully')
            return redirect('topbarEdit')
    else:
        form = TopbarForm(instance=topbar)
    context = {
        'form': form,
        'topbar': topbar,
    }
    return render(request, 'business/sitesettings/topbarEdit.html', context)


def topbarToggleEnable(request):
    event = request.GET.get('event')
    business = Business.objects.get(user=request.user)
    topbar = get_object_or_404(Topbar, business=business)
    if event == 'true':
        topbar.is_enabled = True
        topbar.save()
        result = 'enabled'
    else:
        topbar.is_enabled = False
        topbar.save()
        result = 'disabled'
    return HttpResponse(result)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def socialIcons(request):
    business = Business.objects.get(user=request.user)
    social_icons = SocialMediaLink.objects.filter(business=business).order_by('created_date')
    context = {
        'social_icons': social_icons,
    }
    return render(request, 'business/sitesettings/socialIcons.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def addIcon(request):
    business = Business.objects.get(user=request.user)
    social_icons = SocialMediaLink.objects.filter(business=business)
    form = SocialMediaLinkForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            socialicon = form.save(commit=False)
            socialicon.business = business
            form.save()
            messages.success(request, 'Social icon saved successfully.')
            return redirect('socialIcons')
    else:
        form = SocialMediaLinkForm()
    context = {
        'form': form,
    }
    return render(request, 'business/sitesettings/addIcon.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def editIcon(request, pk=None):
    social_icons = get_object_or_404(SocialMediaLink, pk=pk)

    if request.method == 'POST':
        form = SocialMediaLinkForm(request.POST, instance=social_icons)
        if form.is_valid():
            form.save()
            messages.success(request, 'Social Icon updated successfully.')
            return redirect('socialIcons')
    else:
        form = SocialMediaLinkForm(instance=social_icons)
    context = {
        'form': form,
        'social_icons': social_icons,
    }
    return render(request, 'business/sitesettings/editIcon.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def deleteIcon(request, pk=None):
    social_icon = get_object_or_404(SocialMediaLink, pk=pk)
    social_icon.delete()
    messages.success(request, 'Social Icon has been deleted.')
    return redirect('socialIcons')


def editPolicy(request):
    business = Business.objects.get(user=request.user)
    policy = get_object_or_404(Policy, business=business)
    if request.method == 'POST':
        form = PolicyForm(request.POST, instance=policy)
        if form.is_valid():
            policy = form.save(commit=False)
            policy.business = business
            form.save()
            messages.success(request, 'Policy saved successfully')
            return redirect('editPolicy')
        else:
            print(form.errors)
    else:
        form = PolicyForm(instance=policy)
    context = {
        'form': form,
    }
    return render(request, 'business/sitesettings/editPolicy.html', context)


def editTermsConditions(request):
    business = Business.objects.get(user=request.user)
    terms = get_object_or_404(TermsAndCondition, business=business)
    if request.method == 'POST':
        form = TermsAndConditionForm(request.POST, instance=terms)
        if form.is_valid():
            terms = form.save(commit=False)
            terms.business = business
            form.save()
            messages.success(request, 'Terms & Conditions saved successfully')
            return redirect('editTermsConditions')
        else:
            print(form.errors)
    else:
        form = TermsAndConditionForm(instance=terms)
    context = {
        'form': form,
    }
    return render(request, 'business/sitesettings/editTermsConditions.html', context)
