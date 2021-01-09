from .models import Cart, CartItem, ShopCart, Tax
from .views import _cart_id, shopcart
from category.models import Category
from accounts.models import Business
from urllib.parse import urlparse


def counter(request):
    current_user = request.user
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart_items = ShopCart.objects.all().filter(user_id=current_user.id)
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)



# Cart method
def shopcart_context(request):
    category = Category.objects.all()
    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)

    total=0
    tax = 0
    grand_total = 0
    for i in shopcart:
        total += i.variant.price * i.quantity

    url = request.build_absolute_uri()
    domain = urlparse(url).netloc
    biz_id = Business.objects.get(domain_name=domain)
    get_tax = Tax.objects.get(business__business_id=biz_id.business_id)
    tax_percent = get_tax.tax_percentage
    tax = round((tax_percent * total)/100, 2)
    grand_total = round(total + tax, 2)
    test_context = 'This is test'
    return dict(shopcart=shopcart, category=category, total=total, tax_percent=tax_percent, tax=tax, grand_total=grand_total, test_context=test_context)
