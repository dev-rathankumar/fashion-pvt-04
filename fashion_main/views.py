from django.core.mail import message
from newsletters.models import NewsletterUser
from products.models import Variants
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render


def custom_error_500(request):
    return render(request, '500.html', {})

def custom_error_403(request, exception):
    return render(request, '403.html', {})


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


def ajaxVarUrl(request):
    data = {}
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('productid')
        selectedKey = request.POST.get('selectedKey')
        var_value = request.POST.get('var_value')
        firstKey = request.POST.get('firstKey')
        firstVal = request.POST.get('firstVal')
        urlParams = request.POST.get('urlParams')
        d = dict(x.split("=") for x in urlParams.split("&"))
        dictA = {}
        for key, value in d.items():
            dictA[key] = value
        # {'Size': 'Large', 'Color': 'Blue', 'Place': 'Mumbai', 'Material': 'Silk'}

        variants = Variants.objects.filter(product_id=product_id)
        v = []
        id = []
        for i in variants:
            v.append(i.variant_data)
            id.append(i.id)
        print(v)

        c = 0
        for i in v[:1]:
            for j in i:
                c+=1
        
        Varitem = None
        VarPrice = None
        varId = None
        message = ''
        if c == len(dictA):
            if dictA in v:
                index = v.index(dictA)
                item_id = id[index]
                Varitem = Variants.objects.get(product_id=product_id, id=item_id)
                VarPrice = Varitem.price
                varId = Varitem.id
            else:
                message = 'Out of Stock'
        
        
        # {'Size': 'Medium', 'Color': 'Blue', 'Place': 'Mumbai', 'Material': 'Cotton'}
        # {'Size': 'Large', 'Color': 'Blue', 'Place': 'Delhi', 'Material': 'Silk'}
        # {'Size': 'Small', 'Color': 'Green', 'Place': 'Karnataka', 'Material': 'Linen'}
        # {'Size': 'Large', 'Color': 'Red', 'Place': 'Mumbai', 'Material': 'Silk'}
            
        
        qs = Variants.objects.filter(product_id=product_id, variant_data__contains={firstKey:firstVal})
        
        listDict = []
        for i in qs:
            var_data = i.variant_data
            listDict.append(var_data)
        
        varDict = {}
        for d in listDict:
            for k, v in d.items():
                varDict.setdefault(k, set()).add(v)
        
        

        
        first_key = list(varDict.keys())[0]
        
        selDict = []
        product_variants = Variants.objects.filter(product_id=product_id)
        for i in product_variants:
            selData = i.variant_data
            v = selData[first_key]
            selDict.append(v)
       
        selDict = set(selDict)
        
        context = {
            'varDict': varDict,
            'selectedKey': selectedKey,
            'var_value': var_value,
            'selDict': selDict,
            'first_key': first_key,
            'product_id': product_id,
            'Varitem': Varitem,
        }
        
        data = {'rendered_table': render_to_string('shop/variant_list.html', context=context), 'VarPrice': VarPrice, 'varId': varId, 'message': message}
        return JsonResponse(data)
    return JsonResponse(data)


def unsubscribeNewslt(request):
    email = request.GET.get('email')
    hash = request.GET.get('hash')
    message = ''
    try:
        chkEmail = NewsletterUser.objects.get(email=email, hash=hash)
        chkEmail.delete()
        message = 'unsubscribed'
    except:
        message = 'invalid'
    context = {
        'message': message,
    }
    return render(request, 'pages/unsubscribeNewslt.html', context)