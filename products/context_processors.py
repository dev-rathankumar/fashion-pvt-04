from .models import Wishlist, Product
from django.db.models import Max, Min

def wish_counter(request):
    current_user = request.user
    wish_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            wishlist = Wishlist.objects.all().filter(user_id=current_user.id)
            for wish in wishlist:
                wish_count += 1
        except Wishlist.DoesNotExist:
            wish_count = 0
    return dict(wish_count=wish_count)



def max_product_price(request):
    get_max_price = Product.objects.aggregate(Max('price'))
    for k,v in get_max_price.items():
        max_price = int(v)
    get_min_price = Product.objects.aggregate(Min('price'))
    for k,v in get_min_price.items():
        min_price = int(v)
    return dict(min_price=min_price, max_price=max_price)
