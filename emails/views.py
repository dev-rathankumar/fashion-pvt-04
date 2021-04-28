from django.shortcuts import render, redirect
from .models import Email
from .forms import EmailForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from accounts.models import User
from django.http import HttpResponse

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
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
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
