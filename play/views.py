from django.core import exceptions
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

# Create your views here.


def sya_hello(request):
    #return HttpResponse("Hello world")
    #queryset = Product.objects.all()
    try:
        product = Product.objects.get(pk=0)
    except ObjectDoesNotExist:
        pass
    #product = Product.objects.filter(pk=1).first()
    exist = Product.objects.filter(pk=1).exists()
    #list(query_set)
    #for product in query_set:
    #    print(product)

    return render(request,'hello.html',{'name':'Suresh'})
