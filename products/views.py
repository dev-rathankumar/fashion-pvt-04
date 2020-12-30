from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductGallery, Wishlist, WishlistForm, Size
from .models import Category, Variants, Color, Compare, CompareItem
from .models import ReviewRating, ReviewForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from carts.models import ShopCart, ShopCartForm
from django.db.models import Q
from django.db.models import Max

from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def shop(request, slug=None):
    categories = None
    products = None
    popular_products = None

    sizes = Size.objects.values_list('name', flat=True).distinct()
    colors = Color.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))

    if 'min-price' in request.GET:
        min_price = request.GET['min-price']
        max_price = request.GET['max-price']
        if max_price:
            products = Product.objects.filter(price__gte=min_price, price__lte=max_price)

    if 'size' in request.GET:
        size = request.GET.getlist('size') # ['M', 'XL']
        size_id = Size.objects.filter(name__in=size).values_list('id', flat=True)  # [2, 3, 4]
        product = Variants.objects.filter(size__in=size_id).values_list('product', flat=True)  # [ 1, 2 ]
        products = Product.objects.filter(id__in=product)

    if 'color' in request.GET:
        color = request.GET.getlist('color')
        color_id = Color.objects.filter(name__in=color).values_list('id', flat=True)  # [2, 3, 4]
        product = Variants.objects.filter(color__in=color_id).values_list('product', flat=True)  # [ 1, 2 ]
        products = Product.objects.filter(id__in=product)

    if slug != None:
        categories = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=categories, is_available=True, is_active=True)
        paginator = Paginator(products, 10)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
        popular_products = Product.objects.all().filter(is_available=True, is_active=True, is_popular=True).order_by('id')
    else:
        products = Product.objects.all().filter(is_available=True, is_active=True).order_by('id')
        paginator = Paginator(products, 10)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
        popular_products = Product.objects.all().filter(is_available=True, is_active=True, is_popular=True).order_by('id')

    context = {
        'products': paged_products,
        'product_count': product_count,
        'popular_products': popular_products,
        'sizes': sizes,
        'colors': colors,
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

    get_id = Product.objects.get(slug=product_slug)
    id = get_id.id

    # Get reviews and ratings
    reviews = ReviewRating.objects.filter(product_id=id, status=True)

    # Check if this product is added to comparision
    is_added_to_compare = None
    try:
        compare = Compare.objects.get(compare_id=_compare_id(request))
        is_added_to_compare = CompareItem.objects.filter(product=product, compare=compare)
    except Compare.DoesNotExist:
        pass

    context = {
        'single_product': single_product,
        'gallery': gallery,
        'reviews': reviews,
        'is_added_to_compare': is_added_to_compare,
    }

    query = request.GET.get('q')
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
                        'variant': variant,'query': query,
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
    product = Product.objects.get(pk=id)
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


def search(request):
    products = None
    product_count = 0

    sizes = Size.objects.values_list('name', flat=True).distinct()
    colors = Color.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()

    if 'min-price' in request.GET:
        min_price = request.GET['min-price']
        max_price = request.GET['max-price']
        if max_price:
            products = Product.objects.filter(price__gte=min_price, price__lte=max_price)
            product_count = products.count()

    if 'size' in request.GET:
        size = request.GET.getlist('size') # ['M', 'XL']
        size_id = Size.objects.filter(name__in=size).values_list('id', flat=True)  # [2, 3, 4]
        product = Variants.objects.filter(size__in=size_id).values_list('product', flat=True)  # [ 1, 2 ]
        products = Product.objects.filter(id__in=product)
        product_count = products.count()

    if 'color' in request.GET:
        color = request.GET.getlist('color')
        color_id = Color.objects.filter(name__in=color).values_list('id', flat=True)  # [2, 3, 4]
        product = Variants.objects.filter(color__in=color_id).values_list('product', flat=True)  # [ 1, 2 ]
        products = Product.objects.filter(id__in=product)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
        'sizes': sizes,
        'colors': colors,
        # 'values' : request.GET,
    }

    return render(request, 'shop/shop.html', context)


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            review = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance = review) # Update existing record
            form.save()
            messages.success(request, "Thank you! Your review has been updated.")
            return HttpResponseRedirect(url)

        except ReviewRating.DoesNotExist:
                form = ReviewForm(request.POST) # Save new record
                if form.is_valid():
                    data = ReviewRating()
                    data.subject = form.cleaned_data['subject']
                    data.review = form.cleaned_data['review']
                    data.rating = form.cleaned_data['rating']
                    data.ip = request.META.get('REMOTE_ADDR')
                    data.product_id=product_id
                    data.user_id = request.user.id
                    data.save()
                    messages.success(request, "Thank you! Your review has been submitted.")
                    return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)


# Get the session_id
def _compare_id(request):
    compare = request.session.session_key
    if not compare:
        compare = request.session.create()
    return compare


# Product comparison
def compare_products(request):
    compare_product_1 = None
    compare_product_2 = None
    compare_count = 0
    try:
        compare = Compare.objects.get(compare_id=_compare_id(request))
        compare_products = CompareItem.objects.filter(compare=compare)
        compare_count = compare_products.count()
        if compare_count == 1:
            compare_product_1 = compare_products[0]
        elif compare_count == 2:
            compare_product_1 = compare_products[0]
            compare_product_2 = compare_products[1]
    except Compare.DoesNotExist:
        pass

    context = {
        'compare_product_1': compare_product_1,
        'compare_product_2': compare_product_2,
        'compare_count' : compare_count,
    }
    return render(request, 'shop/compare_products.html', context)


def add_to_compare(request, product_id):
    url = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id) # get the product
    try:
        compare = Compare.objects.get(compare_id=_compare_id(request)) # get the compare object using the session_id present in the session
    except Compare.DoesNotExist:
        compare = Compare.objects.create(
            compare_id = _compare_id(request)
        )
    compare.save()

    compare_count = CompareItem.objects.filter(compare=compare).count()
    if compare_count >= 2:
        messages.warning(request, 'You cannot add more than 2 products to compare.')
        return HttpResponseRedirect(url)
    else:
        try:
            compare_item = CompareItem.objects.get(product=product, compare=compare)
            if compare_item:
                messages.warning(request, 'This product is already exists. Please add different product.')
                return HttpResponseRedirect(url)
        except CompareItem.DoesNotExist:
            compare_item = CompareItem.objects.create(
                product = product,
                compare = compare,
            )
            compare_item.save()
            messages.success(request, 'Product has been added to compare')
    return HttpResponseRedirect(url)


def remove_from_compare(request, product_id):
    url = request.META.get('HTTP_REFERER')
    compare = Compare.objects.get(compare_id=_compare_id(request))
    product = get_object_or_404(Product, id=product_id)
    compare_item = CompareItem.objects.get(product=product, compare=compare)
    compare_item.delete()
    return HttpResponseRedirect(url)
