from django.shortcuts import render
from accounts.models import Business
from .models import Inquiry
from django.core.mail import send_mail

from django.http import HttpResponse

def inquiry(request):
    if request.method == 'POST':
        business_id = request.POST['business_id']
        user_id = request.POST['user_id']
        product_id = request.POST['product_id']
        product_name = request.POST['product_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        inq_message = request.POST['inq_message']

        business = Business.objects.get(business_id=business_id)


        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Inquiry.objects.all().filter(product_id=product_id, user_id=user_id)
            if has_contacted:
                return HttpResponse('already-inquired')

        inquiry = Inquiry(business=business, user_id=user_id, product_id=product_id,
        product_name=product_name, first_name=first_name, last_name=last_name, email=email,
        phone=phone, inq_message=inq_message)

        business_email = business.user.email
        send_mail(
                'New Product Inquiry',
                'You have a new inquiry for the product ' + product_name + '.',
                'rathan.kumar049@gmail.com',
                [business_email],
                fail_silently=False,
            )

        inquiry.save()
        return HttpResponse('Your inquiry has been submitted. Our representative will get in touch with you soon.')
