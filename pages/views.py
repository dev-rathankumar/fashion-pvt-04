from django.shortcuts import render
from category.models import Category
from products.models import Product, ProductGallery
from accounts.models import Business
from sitesettings.models import AboutContent, BannerImage, StoreFeature, ParallaxBackground, Homepage, ContactPage, SocialMediaLink, AboutPage, Policy, TermsAndCondition
from urllib.parse import urlparse

from django.http import HttpResponse

# Create your views here.
def home(request):
    """Home Page"""
    categories = Category.objects.filter(parent=None).order_by('created_date')[:3]
    banners = BannerImage.objects.all()
    features = StoreFeature.objects.all()

    url = request.build_absolute_uri()
    domain = urlparse(url).netloc
    try:
        business = Business.objects.get(domain_name=domain)
    except:
        business = None

    if business is None:
        return HttpResponse('<h3>Please assign a business to proceed!</h3>')
    try:
        background = ParallaxBackground.objects.get(homepage__business=business)
    except:
        background= None

    new_arrival_products = Product.objects.filter(is_active=True).order_by('-created_date')
    context = {
        'categories': categories,
        'banners': banners,
        'features': features,
        'background': background,
        'new_arrival_products': new_arrival_products,
    }




    return render(request, 'pages/home.html', context)

def about(request):
    """About Page"""
    url = request.build_absolute_uri()
    domain = urlparse(url).netloc
    try:
        business = Business.objects.get(domain_name=domain)
    except:
        business = None
    if business is None:
        return HttpResponse('<h3>Please assign a business to proceed!</h3>')
    about_page = AboutPage.objects.get(business=business)
    aboutContents = AboutContent.objects.filter(about_id=about_page).order_by('created_date')


    context = {
        'about_page': about_page,
        'aboutContents': aboutContents,
    }
    return render(request, 'pages/about.html', context)


def contact_page(request):
    """Contact Page"""
    url = request.build_absolute_uri()
    domain = urlparse(url).netloc
    try:
        business = Business.objects.get(domain_name=domain)
    except:
        business = None
    if business is None:
        return HttpResponse('<h3>Please assign a business to proceed!</h3>')
    contact_page = ContactPage.objects.get(business=business)

    # get social media icons
    social_icons = SocialMediaLink.objects.filter(business=business).order_by('created_date')
    context = {
        'contact_page': contact_page,
        'social_icons': social_icons,
    }
    return render(request, 'pages/contact.html', context)


def privacy_policy(request):
    """Privacy Policy Page"""
    url = request.build_absolute_uri()
    domain = urlparse(url).netloc
    try:
        business = Business.objects.get(domain_name=domain)
    except:
        business = None
    if business is None:
        return HttpResponse('<h3>Please assign a business to proceed!</h3>')
    policy = Policy.objects.get(business=business)

    context = {
        'policy': policy,
    }
    return render(request, 'pages/privacy_policy.html', context)


def terms_and_conditions(request):
    """Terms & Conditions Page"""
    url = request.build_absolute_uri()
    domain = urlparse(url).netloc
    try:
        business = Business.objects.get(domain_name=domain)
    except:
        business = None
    if business is None:
        return HttpResponse('<h3>Please assign a business to proceed!</h3>')
    terms = TermsAndCondition.objects.get(business=business)

    context = {
        'terms': terms,
    }
    return render(request, 'pages/terms_and_conditions.html', context)
