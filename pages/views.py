from django.shortcuts import redirect, render
from category.models import Category
from products.models import Product, ProductGallery
from accounts.models import Business
from sitesettings.models import AboutContent, BannerImage, Service, ServiceActivation, StoreFeature, ParallaxBackground, Homepage, ContactPage, SocialMediaLink, AboutPage, Policy, TermsAndCondition
from urllib.parse import urlparse

from django.http import HttpResponse
from django.utils.translation import gettext as _



# Custom decorator to check if the service feature is enabled or not
def is_service_activated(func):
    def wrapper(request, *args, **kwargs):
        url = request.build_absolute_uri()
        domain = urlparse(url).netloc
        try:
            business = Business.objects.get(domain_name=domain)
            service_activation = ServiceActivation.objects.get(business=business)
            if not service_activation.is_enabled:
                return redirect('home')
        except:
            pass
        return func(request, *args, **kwargs)
    return wrapper


def home(request):
    """Home Page"""
    # Set the language session key manually
    # user_language = 'es'
    # translation.activate(user_language)
    # request.session[translation.LANGUAGE_SESSION_KEY] = user_language

    # if translation.LANGUAGE_SESSION_KEY in request.session:
    #     del request.session[translation.LANGUAGE_SESSION_KEY]

    title = _('Homepage')

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
        'title': title,
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


@is_service_activated
def services(request):
    services = Service.objects.filter(is_active=True).order_by('created_date')
    context = {
        'services': services,
    }
    return render(request, 'pages/services.html', context)