from django.shortcuts import render
from accounts.models import Business
from .models import Inquiry
from django.core.mail import send_mail
from datetime import datetime
import time
from datetime import timedelta

from .models import SiteContact
import random
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




def contact(request):
    if request.method == 'POST':
        business_id = request.POST['business_id']
        user_id = request.POST['user_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        contact_message = request.POST['contact_message']

        business = Business.objects.get(business_id=business_id)

        otp = str(random.randint(100000,999999))
        contact = SiteContact(business=business, user_id=user_id, name=name, email=email,
        phone=phone, subject=subject, contact_message=contact_message, otp = otp)
        contact.save()

        business_name = str(business) # because we cannot pass Business directly.
        email_body = 'Hi ' + name + ', ' + 'Your One Time Password for contacting ' + business_name + ' is ' + otp + '.'

        send_mail(
                'Your One Time Password is here',
                email_body,
                'rathan.kumar049@gmail.com',
                [email],
                fail_silently=False,
            )
        contact.is_otp_sent = True
        contact.save()
        request.session['email'] = email
        request.session['id'] = contact.id
        request.session['business_email'] = business.user.email
        return HttpResponse('otp sent')
    else:
        return render(request, 'pages/contact.html')


def verify_otp(request):
    email = request.session['email']
    id = request.session['id']
    business_email = request.session['business_email']
    if request.method == 'POST':
        otp = request.POST.get('otp')
        contact = SiteContact.objects.get(email=email, id=id)
        # get otp updated time
        get_updated_time = contact.otp_updated_time
        datetime_get_updated_time = datetime.strptime(get_updated_time, '%Y-%m-%d %H:%M:%S.%f')
        current_time = datetime.now()
        difference = (current_time - datetime_get_updated_time).total_seconds() # convert difference time to seconds
        if difference >= 90:
            contact.is_otp_expired = True
            contact.save()
            return HttpResponse('Invalid OTP')
        else:
            if contact.otp == otp:
                send_mail(
                        'You have a new message from Website contact form',
                        'Name:' + contact.name + '.' + 'Email:' + contact.email + '.' + 'Phone:' + contact.phone + '.' + 'Subject:' + contact.subject + '.' + 'Message:' + contact.contact_message + '.',
                        'rathan.kumar049@gmail.com',
                        [business_email],
                        fail_silently=False,
                    )
                contact.is_otp_verified = True
                contact.save()
                return HttpResponse('verified')
            else:
                return HttpResponse('wrong-otp')


def resend_otp(request):
    email = request.session['email']
    id = request.session['id']
    business_email = request.session['business_email']
    contact = SiteContact.objects.get(email=email, id=id)
    if contact.is_otp_verified:
        return HttpResponse('Your OTP is already verified')
    else:
        try:
            otp = str(random.randint(100000,999999))
            contact = SiteContact.objects.get(email=email, id=id)
            contact.otp = otp
            contact.save()
            if contact.otp_resend_counter >= 3:
                return HttpResponse('You have exceeded the maximum attempts of resending OTP. Please try different email address.')
            else:
                business_name = contact.business
                email_body = 'Hi ' + contact.name + ', ' + 'Your One Time Password for contacting ' + str(business_name) + ' is ' + contact.otp + '.'
                send_mail(
                        'Your One Time Password is here',
                        email_body,
                        'rathan.kumar049@gmail.com',
                        [email],
                        fail_silently=False,
                    )
                contact.otp_resend_counter += 1
                contact.save()
                return HttpResponse('otp sent')
        except:
            pass
