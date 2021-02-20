from django.shortcuts import render, redirect
from django.http import HttpResponse
from carts.models import ShopCart, Tax
from products.models import Product
from .models import OrderForm, Order, OrderProduct
from django.utils.crypto import get_random_string
from django.contrib import messages
from accounts.models import Business
from urllib.parse import urlparse
import datetime
from django.core.mail import send_mail

# Create your views here.
def orderproduct(request):
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    cart_count = shopcart.count()
    if cart_count <= 0:
        return redirect('shop')
    # Calculate Grand Total
    total=0
    tax = 0
    grand_total = 0
    tax_percent = 0
    for i in shopcart:
        total += i.variant.price * i.quantity

    url = request.build_absolute_uri()
    domain = urlparse(url).netloc
    biz_id = Business.objects.get(domain_name=domain)

    try:
        get_tax = Tax.objects.get(business__business_id=biz_id.business_id)
        tax_percent = get_tax.tax_percentage
        tax = round((tax_percent * total)/100, 2)
    except Tax.DoesNotExist:
        tax = 0
    grand_total = round(total + tax, 2)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Send credit card info to bank and get the result.

            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.user_id = current_user.id
            data.total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            # Generate Order Number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d")
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            # Move cart items to Order Products table
            shopcart = ShopCart.objects.filter(user_id=current_user.id)
            for item in shopcart:
                orderproduct = OrderProduct()
                orderproduct.order_id = data.id # Order Id
                orderproduct.product_id = item.product_id
                orderproduct.variant_id = item.variant.id
                orderproduct.user_id = current_user.id
                orderproduct.quantity = item.quantity
                orderproduct.color = item.color
                orderproduct.size = item.size
                orderproduct.price = item.variant.price
                orderproduct.amount = item.amount
                orderproduct.save()

                # Reduce quantity of sold products from the product db
                product = Product.objects.get(id=item.product_id)
                product.stock -= item.quantity
                product.save()

            ordered_products = OrderProduct.objects.filter(order_id=orderproduct.order_id)
            order = Order.objects.get(order_number=order_number)
            subtotal = 0
            for i in ordered_products:
                subtotal += i.variant.price * i.quantity

            ShopCart.objects.filter(user_id=current_user.id).delete() # Clear & Delete shopcart
            request.session['cart_items'] = 0
            send_mail(
                    'Thank you for your order!',
                    'Your order has been recieved.',
                    'rathan.kumar049@gmail.com',
                    [order.email],
                    fail_silently=False,
                )

            context = {
                'order_number': order_number,
                'ordered_products': ordered_products,
                'order': order,
                'subtotal': subtotal,
            }
            return render(request, 'orders/order_complete.html', context)
        else:
            messages.error(request, form.errors)
            return redirect('checkout')
    else:
        return redirect('checkout')


def order_complete(request):
    return render(request, 'orders/order_complete.html')
