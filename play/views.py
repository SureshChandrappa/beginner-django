from django.core import exceptions
from django.db.models import Q, F
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItems

# Create your views here.


def sya_hello(request):
    #Sort
    # .values to select using title
    queryset =Product.objects.filter(id__in= OrderItems.objects.values('product_id').distinct()).order_by('title')



    return render(request,'hello.html',{'name':'Suresh','products':list(queryset)})
