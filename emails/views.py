from django.shortcuts import render, redirect, get_object_or_404
from .models import Email, BusinessEmailSetting
from .forms import EmailForm, BusinessEmailSettingForm
from django.contrib import messages
from django.core.mail import get_connection, send_mail
from django.core.mail import EmailMessage
from django.core.mail.message import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from accounts.models import User
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def emails(request):
    emails = Email.objects.all().order_by('-sent_date')
    context = {
        'emails': emails,
    }
    return render(request, 'business/emails/emails.html', context)


def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email_obj = form.save()
            subject = form.cleaned_data['subject']
            email_body = form.cleaned_data['email_body']
            to_address = form.cleaned_data['to_address']
            # Send email
            try:
                user = User.objects.get(email=to_address)
            except User.DoesNotExist:
                pass



            current_site = get_current_site(request)
            mail_subject = subject
            message = render_to_string('business/emails/email_template.html', {
                'user': user,
                'domain': current_site.domain,
                'email_body': email_body,
            })
            to_email = to_address
            # Get Email Connection
            email_settings = BusinessEmailSetting.objects.get(business__user=request.user)
            with get_connection(
                host=email_settings.email_host,
                port=email_settings.port,
                username=email_settings.email_host_user,
                password=email_settings.email_host_password,
                use_tls=email_settings.email_use_tls
            ) as connection:
                email = EmailMessage(mail_subject, message, to=[to_email],
                             connection=connection)
            # email = EmailMessage(
            #     mail_subject, message, to=[to_email]
            # )
            email.content_subtype = "html"
            email.send()
            email_obj.is_sent = True
            email_obj.save()
            messages.success(request, 'Email Sent Successfully.')
            return redirect('emails')
    else:
        form = EmailForm()
    context = {
        'form': form,
    }
    return render(request, 'business/emails/send_email.html', context)


def email_detail(request, pk=None):
    try:
        email = Email.objects.get(pk=pk)
    except Email.DoesNotExist:
        messages.error(request, 'Invalid request. Please try again')
        return redirect('emails')

    context = {
        'email': email,
    }
    return render(request, 'business/emails/email_detail.html', context)


def email_settings(request):
    # email_settings = BusinessEmailSetting.objects.get(business__user=request.user)
    email_settings = get_object_or_404(BusinessEmailSetting, business__user=request.user)
    if request.method == "POST":
        form = BusinessEmailSettingForm(request.POST, instance=email_settings)
        form.save()
        messages.success(request, 'Settings applied successfully.')
        return redirect('email_settings')
    else:
        form = BusinessEmailSettingForm(instance=email_settings)
    context = {
        'form': form,
        # 'background': background,
    }
    return render(request, 'business/emails/email_settings.html', context)
