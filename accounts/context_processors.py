from accounts.models import Business
from urllib.parse import urlparse


def get_business(request):
    url = request.build_absolute_uri()
    domain = urlparse(url).netloc
    business = Business.objects.get(domain_name=domain)
    return dict(business=business)
