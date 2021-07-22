from django.core import exceptions
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

# Create your views here.


def sya_hello(request):
    # inventory > 10 AND unit_price <20
    #queryset = Product.objects.filter(unit_price__gt=10,unit_price__lt=20)
    #queryset = Product.objects.filter(unit_price__gt=10).filter(unit_price__lt=20)
    # inventory >10 OR unitprice < 20 for this we use Q
    queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))

    return render(request,'hello.html',{'name':'Suresh','products':list(queryset)})
