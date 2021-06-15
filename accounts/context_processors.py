from accounts.models import Business, User
from urllib.parse import urlparse
from sitesettings.models import Header, Homepage, Footer, Topbar
from django.http import HttpResponse
from datetime import date, datetime


def get_business(request):
    url = request.build_absolute_uri()
    domain = urlparse(url).netloc
    try:
        business = Business.objects.get(domain_name=domain)
        get_exp_date = business.account_expiry_date
        exp_date = datetime.strptime(str(get_exp_date), '%Y-%m-%d')
        get_today = date.today()
        today = datetime.strptime(str(get_today), '%Y-%m-%d')
        if today > exp_date:
            account_expiry = True
        else:
            account_expiry = False
        return dict(business=business, domain=domain, account_expiry=account_expiry)
    except:
        business = None
    return dict(domain=domain)


def get_sitesettings(request):
    url = request.build_absolute_uri()
    domain = urlparse(url).netloc
    try:
        business = Business.objects.get(domain_name=domain)
        if business:
            company_name = business.company_name
            
            try:
                header = Header.objects.get(business=business)
                footer = Footer.objects.get(business=business)
                topbar = Topbar.objects.get(business=business)
            except:
                header = None
                footer = None
                topbar = None
    except:
        header = None
        footer = None
        topbar = None
        company_name = None
    return dict(header=header, company_name=company_name, footer=footer, topbar=topbar)
