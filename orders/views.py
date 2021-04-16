from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from carts.models import ShopCart, Tax, TaxSetting
from products.models import Product
from .models import OrderForm, Order, OrderProduct, Payment
from django.utils.crypto import get_random_string
from django.contrib import messages
from accounts.models import Business
from urllib.parse import urlparse
import datetime
from django.core.mail import send_mail
import json
from django.core import serializers
from django.conf import settings


def payments(request):
    body = json.loads(request.body)
    print('body-->', body)
    order = Order.objects.get(user=request.user, ordered=False, order_number=body['orderID'])

    # Create and save payment instance
    payment = Payment(
        user = request.user,
        payment_id = body['payID'],
        payment_method = body['paymentMethod'],
        amount = order.total,
        status = body['status'],
    )
    payment.save()

    order.payment = payment
    order.ordered = True
    order.save()

    # Move cart items to Order Products table
    shopcart = ShopCart.objects.filter(user_id=request.user.id)
    for item in shopcart:
        orderproduct = OrderProduct()
        orderproduct.order_id = order.id # Order Id
        orderproduct.payment = payment
        orderproduct.product_id = item.product_id
        orderproduct.variant_id = item.variant.id
        orderproduct.user_id = request.user.id
        orderproduct.quantity = item.quantity
        orderproduct.color = item.color
        orderproduct.size = item.size
        orderproduct.price = item.variant.price
        orderproduct.amount = item.amount
        orderproduct.status = "New"
        orderproduct.ordered = True
        orderproduct.save()

        # Reduce quantity of sold products from the product db
        product = Product.objects.get(id=item.product_id)
        product.stock -= item.quantity
        product.save()

    ordered_products = OrderProduct.objects.filter(order_id=orderproduct.order_id)
    order = Order.objects.get(order_number=order.order_number)
    subtotal = 0
    for i in ordered_products:
        subtotal += i.variant.price * i.quantity

    ShopCart.objects.filter(user_id=request.user.id).delete() # Clear & Delete shopcart
    request.session['cart_items'] = 0
    email_host_user = settings.EMAIL_HOST_USER
    send_mail(
            'Thank you for your order!',
            'Your order has been recieved.',
            email_host_user,
            [order.email],
            fail_silently=False,
        )

    context = {
        'order_number': order.order_number,
        'ordered_products': ordered_products,
        'order': order,
        'subtotal': subtotal,
        'payment': payment,
    }
    data = {
        'order_number': order.order_number,
        'payment_id': payment.payment_id,
    }
    return JsonResponse(data)
    # return render(request, 'orders/order_complete.html', context)
    # return JsonResponse('Payment submitted..', safe=False)
    # return JsonResponse({'order_number':order.order_number})
    # ordered_products_json = serializers.serialize('json', ordered_products, order)
    # return HttpResponse(ordered_products_json, content_type='application/json')
    # return JsonResponse(serializers.serialize('json', order), safe=False)
    # return JsonResponse({
    #     'status_code': 1,
    #     'order_number':order.order_number,
    #     'ordered_products': ordered_products,
    #     'order': order,
    #     'subtotal': subtotal,
    #     'payment': payment,
    # }, safe=False)
    # return redirect('order_complete')
    # return render(request, 'orders/order_complete.html', context)


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

    get_tax = TaxSetting.objects.all()
    tax_dict = {}
    for i in get_tax:
        tax_type = i.tax_type
        tax_value = i.tax_value
        tx_amount = round((tax_value * total)/100, 2)
        tax_dict.update({tax_type: {float(tax_value):float(tx_amount)}})

    tax = sum(x for counter in tax_dict.values() for x in counter.values())
    grand_total = round(float(total) + tax, 2)

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
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.pin_code = form.cleaned_data['pin_code']
            data.note = form.cleaned_data['note']
            data.user_id = current_user.id
            data.total = grand_total
            data.tax_data = tax_dict
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
            request.session['order_number'] = order_number
            order = Order.objects.get(user=current_user, ordered=False, order_number=order_number)
            context = {
                'order' : order,
            }
            return render(request, 'orders/payments.html', context)

            # Move cart items to Order Products table
            # shopcart = ShopCart.objects.filter(user_id=current_user.id)
            # for item in shopcart:
            #     orderproduct = OrderProduct()
            #     orderproduct.order_id = data.id # Order Id
            #     orderproduct.product_id = item.product_id
            #     orderproduct.variant_id = item.variant.id
            #     orderproduct.user_id = current_user.id
            #     orderproduct.quantity = item.quantity
            #     orderproduct.color = item.color
            #     orderproduct.size = item.size
            #     orderproduct.price = item.variant.price
            #     orderproduct.amount = item.amount
            #     orderproduct.save()
            #
            #     # Reduce quantity of sold products from the product db
            #     product = Product.objects.get(id=item.product_id)
            #     product.stock -= item.quantity
            #     product.save()

            # ordered_products = OrderProduct.objects.filter(order_id=orderproduct.order_id)
            # order = Order.objects.get(order_number=order_number)
            # subtotal = 0
            # for i in ordered_products:
            #     subtotal += i.variant.price * i.quantity

            # ShopCart.objects.filter(user_id=current_user.id).delete() # Clear & Delete shopcart
            # request.session['cart_items'] = 0
            # send_mail(
            #         'Thank you for your order!',
            #         'Your order has been recieved.',
            #         'rathan.kumar049@gmail.com',
            #         [order.email],
            #         fail_silently=False,
            #     )

            # context = {
            #     'order_number': order_number,
            #     'ordered_products': ordered_products,
            #     'order': order,
            #     'subtotal': subtotal,
            # }
            # return render(request, 'orders/order_complete.html', context)
        else:
            return redirect('checkout')
    else:
        return redirect('checkout')


def order_complete(request):
    order_number = request.GET.get('order_number')
    transaction_id = request.GET.get('payment_id')

    try:
        order = Order.objects.get(order_number=order_number)
        ordered_products = OrderProduct.objects.filter(order_id=order.id)
        subtotal = 0
        for i in ordered_products:
            subtotal += i.variant.price * i.quantity

        payment = Payment.objects.get(payment_id=transaction_id)
        print(type(order.tax_data))
        context = {
            'order_number': order.order_number,
            'ordered_products': ordered_products,
            'order': order,
            'subtotal': subtotal,
            'transaction_id': payment.payment_id,
        }
        return render(request, 'orders/order_complete.html', context)
    except (Payment.DoesNotExist, Order.DoesNotExist):
        return redirect('home')
