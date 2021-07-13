from sitesettings.models import PaypalConfig
from urllib.parse import urlparse
from accounts.models import Business



def getPaypalClientId(request):
    url = request.build_absolute_uri()
    domain = urlparse(url).netloc
    try:
        business = Business.objects.get(domain_name=domain)
        paypal_config = PaypalConfig.objects.get(business=business)
        print(paypal_config.paypal_client_id)
    except:
        paypal_config = None
    return dict(paypal_config=paypal_config)