from accounts.models import Business, User
from urllib.parse import urlparse
from sitesettings.models import Header, Homepage, Footer
from django.http import HttpResponse


def get_business(request):
    url = request.build_absolute_uri()
    domain = urlparse(url).netloc
    try:
        business = Business.objects.get(domain_name=domain)
    except:
        business = None
    return dict(business=business, domain=domain)


# def get_sitesettings(request):
#     url = request.build_absolute_uri()
#     domain = urlparse(url).netloc
#     try:
#         business = Business.objects.get(domain_name=domain)
#     except:
#         return HttpResponse('Please assign a business to proceed!')
#     company_name = None
#     try:
#         header = Header.objects.get(business=business)
#         footer = Footer.objects.get(business=business)
#     except:
#         header = None
#         footer = None
#         company_name = business.company_name
#     return dict(header=header, company_name=company_name, footer=footer)


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
            except:
                header = None
                footer = None
    except:
        header = None
        footer = None
        company_name = None
    return dict(header=header, company_name=company_name, footer=footer)
