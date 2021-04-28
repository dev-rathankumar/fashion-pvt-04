from accounts.models import Business, User
from urllib.parse import urlparse
from sitesettings.models import Header, Homepage


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
    homepage = None
    try:
        header = Header.objects.get(business=business)
        homepage = Homepage.objects.get(business=business)
    except (Header.DoesNotExist and Homepage.DoesNotExist):
        pass
    return dict(header=header, homepage=homepage)
