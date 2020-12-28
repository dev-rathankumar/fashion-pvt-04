from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .models import Product, ProductGallery, Variants, Wishlist, WishlistForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from carts.models import ShopCart, ShopCartForm

from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def shop(request, slug=None):
    categories = None
    products = None

    if slug != None:
        categories = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=categories, is_available=True, is_active=True)
        paginator = Paginator(products, 10)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True, is_active=True).order_by('id')
        paginator = Paginator(products, 10)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'shop/shop.html', context)



def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        # in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
        product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
        gallery = ProductGallery.objects.filter(product=product)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'gallery': gallery,
        # 'in_cart'       : in_cart,
    }
    query = request.GET.get('q')
    get_id = Product.objects.get(slug=product_slug)
    id = get_id.id
    if product.variant !="None":
        if request.method == 'POST': # if the color is selected
            variant_id = request.POST.get('variantid')
            variant = Variants.objects.get(id=variant_id) # selected product by click color radio button
            colors = Variants.objects.filter(product_id=id,size_id=variant.size_id )
            sizes = Variants.objects.raw('SELECT DISTINCT ON (size_id) * FROM products_variants WHERE product_id=%s ORDER BY size_id',[id])
            query += variant.title+' Size:' +str(variant.size) +' Color:' +str(variant.color)
        else:
            variants = Variants.objects.filter(product_id=id)
            colors = Variants.objects.filter(product_id=id,size_id=variants[0].size_id )
            sizes = Variants.objects.raw('SELECT DISTINCT ON (size_id) * FROM products_variants WHERE product_id=%s ORDER BY size_id',[id])
            variant =Variants.objects.get(id=variants[0].id)
        context.update({'sizes': sizes, 'colors': colors,
                        'variant': variant,'query': query
                        })
    return render(request, 'shop/product_detail.html', context)



@login_required(login_url='/userLogin')
def wishlist(request):
    current_user = request.user  # Access User Session information
    wishlist = Wishlist.objects.filter(user_id=current_user.id)
    context = {
        'wishlist': wishlist,
    }
    return render(request, 'shop/my-wishlist.html', context)


# Add product to wishlist
@login_required(login_url='/userLogin')
def add_to_wishlist(request,product_id):
    id = product_id
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    product= Product.objects.get(pk=id)
    if product.variant != 'None':
        variantid = request.POST.get('variantid')  # from variant add to cart
        checkinvariant = Wishlist.objects.filter(variant_id=variantid, user_id=current_user.id)  # Check product in wishlist
        if checkinvariant:
            control = 1 # The product is in the cart
        else:
            control = 0 # The product is not in the cart"""

    else:
        checkinproduct = Wishlist.objects.filter(product_id=id, user_id=current_user.id) # Check product in wishlist
        if checkinproduct:
            control = 1 # The product is in the cart
        else:
            control = 0 # The product is not in the cart"""


    if request.method == 'POST':  # if there is a post
        form = WishlistForm(request.POST)

        if form.is_valid():
            if control==1: # Already exists
                messages.info(request, 'This product is already in your Wishlist.')
                return HttpResponseRedirect(url)
            else : # Insert to Wishlist
                data = Wishlist()
                data.user_id = current_user.id
                data.product_id =id
                data.variant_id = variantid
                data.quantity = form.cleaned_data['quantity']
                data.save()
                messages.success(request, 'Product added to Wishlist.')
                return HttpResponseRedirect(url)
    else: # if there is no post
        return render(request, 'shop/my-wishlist.html')


def wishlist_addtoshopcart(request, product_id):
    id = product_id
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    product= Product.objects.get(pk=id)
    if product.variant != 'None':
        variantid = request.POST.get('variantid')  # from variant add to cart
        checkinvariant = ShopCart.objects.filter(variant_id=variantid, user_id=current_user.id)  # Check product in shopcart
        if checkinvariant:
            control = 1 # The product is in the cart
        else:
            control = 0 # The product is not in the cart"""

    else:
        checkinproduct = ShopCart.objects.filter(product_id=id, user_id=current_user.id) # Check product in shopcart
        if checkinproduct:
            control = 1 # The product is in the cart
        else:
            control = 0 # The product is not in the cart"""

    if request.method == 'POST':  # if there is a post
        form = ShopCartForm(request.POST)
        # Construct message
        message = 'Product has been added to the cart.'

        wishlist = Wishlist.objects.filter(variant_id=variantid)
        if form.is_valid():
            if control==1: # Update  shopcart
                if product.variant == 'None':
                    data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
                else:
                    data = ShopCart.objects.get(product_id=id, variant_id=variantid, user_id=current_user.id)
                data.quantity += form.cleaned_data['quantity']
                data.save()  # save data
                wishlist.delete()
            else : # Inser to Shopcart
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id =id
                data.variant_id = variantid
                data.quantity = form.cleaned_data['quantity']
                data.save()
                wishlist.delete()
        messages.success(request, message)
        return HttpResponseRedirect(url)

    else: # if there is no post
        if control == 1:  # Update  shopcart
            data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
            data.quantity += 1
            data.save()  #
        else:  #  Insert to Shopcart
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.variant_id =None
            data.save()  #
        messages.success(request, "Product added to Cart")
        return HttpResponseRedirect(url)


def wishlist_delete(request, id):
    wishlist = Wishlist.objects.filter(id=id).delete()
    messages.success(request, "Product has been removed from your Wishlist.")
    return redirect('wishlist')
