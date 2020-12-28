from .models import Category

def category_names(request):
    category = Category.objects.all()
    return dict(category=category)
