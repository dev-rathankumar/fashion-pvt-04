from .models import Wishlist

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

