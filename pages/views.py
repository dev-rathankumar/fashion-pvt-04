from django.shortcuts import render
from category.models import Category

# Create your views here.
def home(request):
    """Home Page"""
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    """About Page"""
    return render(request, 'pages/about.html')

def contact(request):
    """Contact Page"""
    return render(request, 'pages/contact.html')
