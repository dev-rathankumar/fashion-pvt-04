from accounts.models import Business
from urllib.parse import urlparse
from sitesettings.models import Header


def get_business(request):
    url = request.build_absolute_uri()
    domain = urlparse(url).netloc
    business = Business.objects.get(domain_name=domain)
    return dict(business=business)


def get_sitesettings(request):
    url = request.build_absolute_uri()
    domain = urlparse(url).netloc
    business = Business.objects.get(domain_name=domain)
    header = Header.objects.get(business=business)
    return dict(header=header)
