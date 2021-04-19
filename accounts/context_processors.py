from accounts.models import Business
from urllib.parse import urlparse
from sitesettings.models import Header


def get_business(request):
    url = request.build_absolute_uri()
    domain = urlparse(url).netloc
    try:
        business = Business.objects.get(domain_name=domain)
    except:
        business = None
    return dict(business=business, domain=domain)


def get_sitesettings(request):
    url = request.build_absolute_uri()
    domain = urlparse(url).netloc
    try:
        business = Business.objects.get(domain_name=domain)
    except:
        business = None
    header = None
    try:
        header = Header.objects.get(business=business)
    except Header.DoesNotExist:
        pass
    return dict(header=header)
