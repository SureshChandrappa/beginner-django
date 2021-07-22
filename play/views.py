from django.core import exceptions
from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

# Create your views here.


def sya_hello(request):
    #queryset = Product.objects.filter(unit_price__range=(20,30))
    #queryset= Product.objects.filter(title__icontains = 'coffee')
    #case insensitive serch icontains
    queryset = Product.objects.filter(last_updat__year = 2021)

    return render(request,'hello.html',{'name':'Suresh','products':list(queryset)})
