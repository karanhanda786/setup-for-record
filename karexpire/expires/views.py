from django.shortcuts import render
from django.views import generic
from .models import ProductInfo
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request, "karexpire/base.html", {})


class ProductCreate(generic.CreateView):
    fields = ('product_name','expire_at','Company_name')
    model = ProductInfo
    template_name = "karexpire/productinfo_form.html"


# class ProductDetail(generic.ListView):
#     context_object_name = 'productdetail'
#     model= ProductInfo
#     template_name = "karexpire/productdetail_form.html"

def ProductDetail(request):
    qs = ProductInfo.objects.all()
    context = {
        'productdetail':qs
    }
    return render(request, "karexpire/productdetail_form.html", context)

def ProductFind(request):

    boolencheck = False
    qs = ProductInfo.objects.all()
    productName = request.POST.get('product_name')
    expireAt = request.POST.get('expire_at')
    companyName = request.POST.get('Company_name')

    if productName != "" and productName is not None:
        qs = qs.filter(product_name__iexact=productName)
        boolencheck=True

    elif companyName != "" and companyName is not None:
        qs = qs.filter(Company_name__iexact=companyName)
        boolencheck=True

    if expireAt != "" and expireAt is not None:
        qs = qs.filter(expire_at=expireAt)
        boolencheck=True

    context = {
        'productfind':qs,
        'check':boolencheck
    }
    return render(request, "karexpire/productfind_form.html", context)
