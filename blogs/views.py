from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Category

# Create your views here.

from .models import Blog

def blog(request, slug=None):
    blogs = Blog.objects.all().filter(status = 1).order_by('id')
    paginator = Paginator(blogs, 8)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)
    blog_count = blogs.count()
    #popular_products = Product.objects.all().filter(is_available=True, is_active=True, is_popular=True).order_by('id')
    context = {
    'blogs': paged_blogs,
    'blog_count': blog_count,
    }

    return render(request, 'blogs/blogs.html', context)

def blog_detail(request, category_slug, blog_slug):
    try:
        single_blog = Blog.objects.get(category__slug=category_slug, slug=blog_slug)
    except Exception as e:
        raise e
    context = {
        'single_blog': single_blog,}
    return render(request, 'blogs/blog_detail.html', context)


# def product_detail(request, category_slug, blog_slug):
#
#     try:
#         single_blog = Blog.objects.get(category__slug=category_slug, slug=blog_slug)
#         # in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
#         # product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
#         # gallery = ProductGallery.objects.filter(product=product)
#     except Exception as e:
#         raise e
#     # # get business info
#     # url = request.build_absolute_uri()
#     # domain = urlparse(url).netloc
#     # business = Business.objects.get(domain_name=domain)
#     #
#     # get_product_id = Product.objects.get(slug=product_slug)
#     # id = get_product_id.id
#     #
#     # # Get reviews and ratings
#     # reviews = ReviewRating.objects.filter(product_id=id, status=True)
#     #
#     # # Check if this product is added to comparision
#     # is_added_to_compare = None
#     # try:
#     #     compare = Compare.objects.get(compare_id=_compare_id(request))
#     #     is_added_to_compare = CompareItem.objects.filter(product=product, compare=compare)
#     # except Compare.DoesNotExist:
#     #     pass
#     #
#     # if request.user.is_authenticated:
#     #     try:
#     #         orderproduct = OrderProduct.objects.filter(user=request.user, product_id=single_product.id).exists()
#     #     except OrderProduct.DoesNotExist:
#     #         orderproduct = None
#     # else:
#     #     orderproduct = None
#     # print(orderproduct)
#      context = {
#         'single_blog': single_blog,
#
#     }
#
#     # query = request.GET.get('q')
#     # if product.variant !="None":
#     #     if request.method == 'POST': # if the color is selected
#     #         variant_id = request.POST.get('variantid')
#     #         variant = Variants.objects.get(id=variant_id) # selected product by click color radio button
#     #         colors = Variants.objects.filter(product_id=id,size_id=variant.size_id )
#     #         sizes = Variants.objects.raw('SELECT DISTINCT ON (size_id) * FROM products_variants WHERE product_id=%s ORDER BY size_id',[id])
#     #         query += variant.title+' Size:' +str(variant.size) +' Color:' +str(variant.color)
#     #     else:
#     #         variants = Variants.objects.filter(product_id=id)
#     #         colors = Variants.objects.filter(product_id=id,size_id=variants[0].size_id )
#     #         sizes = Variants.objects.raw('SELECT DISTINCT ON (size_id) * FROM products_variants WHERE product_id=%s ORDER BY size_id',[id])
#     #         variant =Variants.objects.get(id=variants[0].id)
#     #
#     #     context.update({'sizes': sizes, 'colors': colors,
#     #                     'variant': variant,'query': query,
#     #                     })
#     return render(request, 'blogs/blog_detail.html', context)
