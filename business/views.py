from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.models import User, Customer, RegionalManager
from accounts.models import Business, TaxOnPlan
from django.http import HttpResponse, JsonResponse
from .forms import PaymentSettingForm
from .models import PaymentSetting
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from datetime import date, datetime
import datetime
import time
import json
from django.contrib import messages
from .forms import UserForm, BusinessForm, ProductForm, ProductGalleryForm, ProductVariantForm
from .forms import CategoryForm, OrderForm, TaxSettingForm
from products.models import Product, ProductGallery, Variants
from django.forms import inlineformset_factory
from django import forms
from django.template.defaultfilters import slugify
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from orders.models import Order, OrderProduct
from plans.models import Plan, PlanOrder, PlanPayment
import json
import ast # for converting tax_data string to dict
from django.template.loader import render_to_string
from carts.models import TaxSetting, Tax
from sitesettings.forms import HeaderForm





# Custom decorator to check whether the user is business or not
def business_required(login_url=None):
    return user_passes_test(lambda u: u.is_business, login_url=login_url)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        try:
            if not user.is_business:
                messages.error(request, "This is not a business account")
                return redirect('userLogin')
        except AttributeError:
            messages.error(request, "Invalid login credentials")
            return redirect('userLogin')

        if user is not None:
            # Check for the expiry date
            biz = Business.objects.get(user__id=user.id)
            get_exp_date = biz.account_expiry_date
            exp_date = datetime.strptime(str(get_exp_date), '%Y-%m-%d')
            get_today = date.today()
            today = datetime.strptime(str(get_today), '%Y-%m-%d')
            if today > exp_date:
                messages.error(request, "Your account is expired.")
                return redirect('userLogin')
            else:
                auth.login(request, user)
                messages.success(request, 'You are now logged in.')
                return redirect('biz_dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('userLogin')
    return render(request, 'business/login.html')


@login_required(login_url = 'userLogin')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('userLogin')
    return redirect('userLogin')



@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def dashboard(request):
    orders = Order.objects.filter(ordered=True)
    orders_count = orders.count()
    revenue = 0
    for i in orders:
        revenue += i.total
    context = {
        'orders_count': orders_count,
        'revenue': revenue,
    }
    return render(request, 'business/dashboard.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def biz_profile(request):
    current_user = request.user
    biz = Business.objects.get(user__id=current_user.id)

    context = {
        'biz': biz,
    }
    return render(request, 'business/profile.html', context)

@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def biz_changePassword(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        user = User.objects.get(username__exact=request.user.username)

        if password == confirm_password:
            success = user.check_password(request.POST['current_password'])
            if success:
                user.set_password(password)
                user.save()
                auth.logout(request)
                messages.success(request, 'Password updated successfully. Please login again.')
                return HttpResponse('success')
            else:
                return HttpResponse('Please enter valid current password')
        else:
            return HttpResponse('Passwords do not match!')
    return render(request, 'business/changePassword.html')


def forgotPassword(request):
    """Send password reset email to Business"""
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)
            if user.is_business == True:
                current_site = get_current_site(request)
                # return HttpResponse(current_site)
                mail_subject = 'Reset Your Password'
                message = render_to_string('business/reset_password_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                to_email = email
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                messages.warning(request, 'Password reset link has been sent to your email address.')
                return redirect('userLogin')
            else:
                messages.warning(request, "This is not a Business account")
                return redirect('biz_forgotPassword')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('biz_forgotPassword')
    else:
        return render(request, 'business/forgotPassword.html')

def resetpassword_validate(request, uidb64, token):
    """Resetting password request validation"""
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('biz_resetForgotPassword')
    else:
        messages.error(request, 'This link has been expired')
        return redirect('biz_forgotPassword')

def biz_resetPassword(request):
    """Reset password"""
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = User.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('userLogin')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('biz_resetForgotPassword')
    else:
        return render(request, 'business/resetPassword.html')


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def editProfile(request, pk=None):
    user = get_object_or_404(User, pk=pk)
    business = get_object_or_404(Business, pk=pk)
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES, instance=user, prefix="user")
        business_form = BusinessForm(request.POST, prefix="business")
        if user_form.is_valid() and business_form.is_valid():
            user = user_form.save()
            business_form.cleaned_data["user"] = user
            current_user = request.user
            biz = Business.objects.get(user=current_user)
            business = business_form.save(commit=False)
            business.user = request.user
            business.is_editing = True
            business.is_verification_email_sent = True
            business.is_account_verified = True
            business.business_id = biz.business_id
            business.domain_name = biz.domain_name
            business.account_activation_date = biz.account_activation_date
            business.account_expiry_date = biz.account_expiry_date
            business.regional_manager = biz.regional_manager
            business.created_date = biz.created_date
            business_form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('/business/editProfile/'+str(pk))
        else:
            print('user form', user_form.errors)
            print('rm form', business_form.errors)
    else:
        user_form = UserForm(instance=user, prefix="user")
        business_form = BusinessForm(instance=business, prefix="business")
    context = {
        'user_form': user_form,
        'business_form': business_form,
        'user': user,
        'business': business,
    }
    return render(request, 'business/editProfile.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def paymentSettings(request, pk=None):
    user = get_object_or_404(User, pk=pk)
    pay_setting = get_object_or_404(PaymentSetting, user=user)
    if request.method == 'POST':
        form = PaymentSettingForm(request.POST, instance=pay_setting)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your payment settings are saved successfully.')
            return redirect('/business/paymentSettings/'+str(pk))
    else:
        form = PaymentSettingForm(instance=pay_setting)

    context = {
        'form': form,
    }
    return render(request, 'business/paymentSettings.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def allProducts(request):
    business = get_object_or_404(Business, pk=request.user.id)
    products = Product.objects.filter(business=business, is_active=True).order_by('-created_date')
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products': paged_products,
    }
    return render(request, 'business/allProducts.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def editProduct(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        basicInfo_form = ProductForm(request.POST, request.FILES, instance=product)
        if basicInfo_form.is_valid():
            basicInfo_form.save()
            return redirect('/business/products/editProduct/'+str(pk)+'/editGallery/')
        else:
            print(basicInfo_form.errors)

    else:
        basicInfo_form = ProductForm(instance=product)
    context = {
        'basicInfo_form': basicInfo_form,
        'product': product,
    }
    return render(request, 'business/editProduct.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def editGallery(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    ProductGalleryFormSet = inlineformset_factory(Product, ProductGallery, form=ProductGalleryForm, extra=1)

    if request.method == 'POST':
        add_another = request.POST['add_another']
        formset = ProductGalleryFormSet(request.POST, request.FILES, instance=product)
        if formset.is_valid():
            formset.save()
            if add_another == 'true':
                return redirect('/business/products/editProduct/'+str(pk)+'/editGallery/')
            else:
                return redirect('/business/products/editProduct/'+str(pk)+'/editVariants/')
        else:
            return HttpResponse(formset.errors)
    else:
        formset = ProductGalleryFormSet(instance=product)
    context = {
        'product' : product,
        'formset': formset,
    }
    return render(request, 'business/editGallery.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def editVariants(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    ProductVariantFormSet = inlineformset_factory(Product, Variants, form=ProductVariantForm, extra=1)

    if request.method == 'POST':
        add_another = request.POST['add_another']
        formset = ProductVariantFormSet(request.POST, instance=product)
        if formset.is_valid():
            formset.save()
            product.is_active = True
            product.save()
            if add_another == 'true':
                return redirect('/business/products/editProduct/'+str(pk)+'/editVariants/')
            else:
                messages.success(request, 'Product has been uploaded successfully.')
                return redirect('allProducts')
        else:
            return HttpResponse(formset.errors)
    else:
        formset = ProductVariantFormSet(instance=product)
        gallery = ProductGallery.objects.filter(product=product)

    context = {
        'product' : product,
        'formset': formset,
        'gallery': gallery,
    }
    return render(request, 'business/editVariants.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def addProduct(request):
    if request.method == 'POST':
        basicInfo_form = ProductForm(request.POST, request.FILES)
        if basicInfo_form.is_valid():
            current_user = request.user
            business_name = Business.objects.get(user=current_user)
            product_name = basicInfo_form.cleaned_data['product_name']
            product = basicInfo_form.save(commit=False)
            product.business = business_name
            product.slug = slugify(product_name)
            basicInfo_form.save()
            pk = product.id
            return redirect('/business/products/editProduct/'+str(pk)+'/editGallery/')
        else:
            print(basicInfo_form.errors)
            messages.error(request, 'Something went wrong!')
            return redirect('allProducts')
    else:
        basicInfo_form = ProductForm()
    context = {
        'basicInfo_form': basicInfo_form,
    }

    return render(request, 'business/addProduct.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def deleteProduct(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, 'Product has been deleted successfully.')
    return redirect('allProducts')



# Manage Categories
@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def allCategories(request):
    categories = Category.objects.filter(is_active=True).order_by('-created_date')
    context = {
        'categories': categories,
    }
    return render(request, 'business/allCategories.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def addCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category = form.save(commit=False)
            category.slug = slugify(category_name)
            form.save()
            messages.success(request, 'Category Added Successfully')
            return redirect('addCategory')
        else:
            print(form.errors)

    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'business/addCategory.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def editCategory(request, pk=None):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category = form.save(commit=False)
            category.slug = slugify(category_name)
            form.save()
            messages.success(request, 'Category Modified Successfully')
            return redirect('allCategories')
        else:
            print(form.errors)

    else:
        form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'business/editCategory.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def deleteCategory(request, pk=None):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, 'Category has been deleted.')
    return redirect('allCategories')


# Manage Orders
@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def allOrders(request):
    orders = Order.objects.filter(ordered=True).order_by('-created_at')
    paginator = Paginator(orders, 10)
    page = request.GET.get('page')
    paged_orders = paginator.get_page(page)
    context = {
        'orders': paged_orders,
    }
    return render(request, 'business/allOrders.html', context)


def bizOrderDetail(request, pk=None):
    try:
        order = Order.objects.get(order_number=pk)
        ordered_products = OrderProduct.objects.filter(order__order_number=pk)
    except Order.DoesNotExist:
        return redirect('allOrders')
    subtotal = 0
    for i in ordered_products:
        subtotal += i.variant.price * i.quantity

    context = {
        'ordered_products': ordered_products,
        'order': order,
        'subtotal': subtotal,
    }
    return render(request, 'business/viewOrder.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def editOrder(request, pk=None):
    order = get_object_or_404(Order, pk=pk)

    # Get ordered products
    try:
        orders = Order.objects.get(pk=pk)
        ordered_products = OrderProduct.objects.filter(order__order_number=order.order_number)
        subtotal = 0
        for i in ordered_products:
            subtotal += i.variant.price * i.quantity
    except Order.DoesNotExist:
        return redirect('allOrders')

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order has been updated.')
            return redirect('allOrders')
        else:
            print(form.errors)

    else:
        form = OrderForm(instance=order)
    context = {
        'form': form,
        'order': order,
        'ordered_products': ordered_products,
        'subtotal': subtotal,
    }
    return render(request, 'business/editOrder.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def deleteOrder(request, pk=None):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    messages.success(request, 'Order has been deleted.')
    return redirect('allOrders')


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def plans(request):
    plans = Plan.objects.all().order_by('plan_price')
    business = Business.objects.get(user=request.user)
    current_plan = Plan.objects.get(pk=business.plan_id)
    context = {
        'plans': plans,
        'current_plan': current_plan,
    }
    return render(request, 'business/plans.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def purchasePlan(request):
    plan_id = request.GET['plan_id']
    try:
        plan = Plan.objects.get(pk=plan_id)
    except Plan.DoesNotExist:
        messages.error(request, 'Invalid request. Please select the plan.')
        return redirect('plans')
    get_tax = TaxOnPlan.objects.all()
    tax_dict = {}
    for i in get_tax:
        tax_type = i.tax_type
        tax_value = i.tax_value
        tx_amount = round((float(tax_value) * plan.plan_price)/100, 2)
        tax_dict.update({tax_type: {float(tax_value):float(tx_amount)}})

    tax = sum(x for counter in tax_dict.values() for x in counter.values())
    print(tax)
    grand_total = round(plan.plan_price + tax, 2)
    context = {
        'plan': plan,
        'tax_dict': tax_dict,
        'grand_total': grand_total,
        'tax': tax,
    }
    return render(request, 'business/purchasePlan.html', context)



def planPayment(request):
    body = json.loads(request.body)
    current_user = request.user
    business = Business.objects.get(user=current_user)
    order = PlanOrder.objects.get(business=business, ordered=False, order_number=body['orderID'])
    # Store transaction details inside payment model

    payment = PlanPayment(
        business = business,
        payment_id = body['transID'],
        payment_method = body['payment_method'],
        amount = body['total'],
        status = body['status'],
    )
    payment.save()




    # Update order model
    order.plan_payment = payment
    if body['status'] == 'COMPLETED':
        order.ordered = True
    else:
        messages.error(request, 'Payment failed. Please try again')
        return redirect('plans')
    order.save()

    # Send order recieved email to customer
    mail_subject = 'Thank you for your order!'
    message = render_to_string('business/plan_order_email.html', {
        'user': request.user,
        'order': order,
    })
    to_email = request.user.email
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    send_email.send()

    # Send order number and transaction id back to sendData method via JsonResponse
    data = {
        'order_number': order.order_number,
        'transID': payment.payment_id,
    }
    return JsonResponse(data)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def planOrder(request):
    current_user = request.user
    if request.method == 'POST':
        plan_id = request.POST['plan_id']
        tax = request.POST['tax']
        tax_data = request.POST['tax_data']
        total = request.POST['total']
        payment_method = request.POST['payment_method']
        plan_price = request.POST['plan_price']

        data = PlanOrder()
        data.business_id = current_user.id
        # data.plan_payment =
        data.plan_id = plan_id
        data.total = total
        data.tax = tax
        data.tax_data = tax_data
        data.ip = request.META.get('REMOTE_ADDR')

        # Calculate Account Manager's Commission
        business = Business.objects.get(user=current_user)
        account_manager = business.regional_manager
        try:
            get_account_manager = RegionalManager.objects.get(user=account_manager)
            commission_percent = get_account_manager.commission_percentage
        except RegionalManager.DoesNotExist:
            commission_percent = 0
        commission_amount = round((commission_percent * float(plan_price))/100, 2)
        data.account_manager_commission = commission_amount
        data.save()
        # Generate Plan Order Number
        yr = int(datetime.date.today().strftime('%Y'))
        dt = int(datetime.date.today().strftime('%d'))
        mt = int(datetime.date.today().strftime('%m'))
        d = datetime.date(yr,mt,dt)
        current_date = d.strftime("%Y%m%d")
        order_number = 'P'+current_date + str(data.id)
        data.order_number = order_number
        data.save()
        request.session['plan_order_number'] = order_number
        business = Business.objects.get(user=current_user)
        try:
            plan_order = PlanOrder.objects.get(business=business, ordered=False, order_number=order_number)
        except PlanOrder.DoesNotExist:
            plan_order = None
    else:
        return redirect('plans')
    # Converting tax_data string to dict for better looping in the template
    tax_data = ast.literal_eval(tax_data)
    context = {
        'plan_order': plan_order,
        'tax': tax,
        'tax_data': tax_data,
        'total': total,
        'payment_method': payment_method,
    }
    return render(request, 'business/planPayment.html', context)



def plan_order_complete(request):
    order_number = request.GET.get('order_number')
    transaction_id = request.GET.get('payment_id')

    try:
        order = PlanOrder.objects.get(order_number=order_number)
        payment = PlanPayment.objects.get(payment_id=transaction_id)

        context = {
            'order': order,
            'payment': payment,
        }
        return render(request, 'business/plan_order_complete.html', context)
    except (Payment.DoesNotExist, Order.DoesNotExist):
        return redirect('plans')


def allCustomers(request):
    customers = Customer.objects.filter(user__is_customer=True).order_by('-created_date')
    paginator = Paginator(customers, 10)
    page = request.GET.get('page')
    paged_customers = paginator.get_page(page)
    context = {
        'customers': paged_customers,
    }
    return render(request, 'business/allCustomers.html', context)


def CustomerViewProfile(request, pk=None):
    try:
        customer = Customer.objects.get(user__id=pk, user__is_customer=True)
    except Customer.DoesNotExist:
        messages.error(request, 'Invalid request. Please try again')
        return redirect('allCustomers')

    context = {
        'customer': customer,
    }
    return render(request, 'business/CustomerViewProfile.html', context)


def setTax(request, pk=None):
    # try:
    #     tax = TaxSetting.objects.get(pk=pk)
    # except:
    #     tax = 0
    business = Business.objects.get(user=request.user)
    tax = get_object_or_404(TaxSetting, pk=pk)
    for i in tax:
        print(i)
    if request.method == 'POST':
        form = PaymentSettingForm(request.POST, instance=pay_setting)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your payment settings are saved successfully.')
            return redirect('/business/paymentSettings/'+str(pk))
    else:
        form = PaymentSettingForm(instance=pay_setting)

    context = {
        'form': form,
    }
    return render(request, 'business/setTax.html')


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def setTax(request, business_id=None):
    tax = get_object_or_404(Tax, business_id=business_id)
    TaxSettingFormSet = inlineformset_factory(Tax, TaxSetting, form=TaxSettingForm, extra=1)

    if request.method == 'POST':
        add_another = request.POST['add_another']
        formset = TaxSettingFormSet(request.POST, instance=tax)
        if formset.is_valid():
            formset.save()
            tax.save()
            if add_another == 'true':
                return redirect('setTax', business_id)
            else:
                messages.success(request, 'Tax Added Successfully.')
                return redirect('setTax', business_id)
        else:
            return HttpResponse(formset.errors)
    else:
        formset = TaxSettingFormSet(instance=tax)

    context = {
        'tax' : tax,
        'formset': formset,
    }
    return render(request, 'business/setTax.html', context)


@login_required(login_url = 'userLogin')
@business_required(login_url="userLogin")
def initial_setup(request):
    # if request.method == 'POST':
    #     form = HeaderForm(request.POST)
    #     if form.is_valid():
    #         store_name = form.cleaned_data['site_title']
    #         form.save()
    #         messages.success(request, 'You are successfully logged in')
    #         return redirect('business')
    #     else:
    #         print(form.errors)
    # else:
    form = HeaderForm()
    context = {
        'form': form,
    }
    return render(request, 'business/initial_setup.html', context)
