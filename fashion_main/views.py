from products.models import Variants
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string


def ajaxcolor(request):
    data = {}
    if request.POST.get('action') == 'post':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        colors = Variants.objects.filter(product_id=productid, size_id=size_id)
        context = {
            'size_id': size_id,
            'productid': productid,
            'colors': colors,
        }
        data = {'rendered_table': render_to_string('shop/color_list.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)
