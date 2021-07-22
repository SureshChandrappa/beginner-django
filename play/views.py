from django.core import exceptions
from django.db.models import Q, F
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

# Create your views here.


def sya_hello(request):
    #Sort
    #queryset = Product.objects.order_by('title')
    queryset = Product.objects.order_by('inventory','-title').reverse()

    return render(request,'hello.html',{'name':'Suresh','products':list(queryset)})
