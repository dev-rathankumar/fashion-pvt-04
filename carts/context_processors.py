from .models import Cart, CartItem, ShopCart
from .views import _cart_id, shopcart

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
