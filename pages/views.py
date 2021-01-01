from django.shortcuts import render
from category.models import Category
from products.models import Product, ProductGallery

from django.http import HttpResponse

# Create your views here.
def home(request):
    """Home Page"""
    category = Category.objects.all()
    context = {
        'category': category,
    }

    new_arrival_products = Product.objects.filter(is_active=True).order_by('-created_date')
    context.update({
        'new_arrival_products': new_arrival_products,
    })
    return render(request, 'pages/home.html', context)

def about(request):
    """About Page"""
    return render(request, 'pages/about.html')
