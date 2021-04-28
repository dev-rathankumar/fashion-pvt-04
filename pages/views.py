from django.shortcuts import render
from category.models import Category
from products.models import Product, ProductGallery
from accounts.models import Business
from sitesettings.models import BannerImage, StoreFeature, ParallaxBackground, Homepage
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

    homepage = Homepage.objects.get(business=business)
    background = ParallaxBackground.objects.get(homepage=homepage)
    context = {
        'categories': categories,
        'banners': banners,
        'features': features,
        'background': background
    }

    new_arrival_products = Product.objects.filter(is_active=True).order_by('-created_date')
    context.update({
        'new_arrival_products': new_arrival_products,
    })
    return render(request, 'pages/home.html', context)

def about(request):
    """About Page"""
    return render(request, 'pages/about.html')
