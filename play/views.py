from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calculate():
    x=2
    return x

def sya_hello(request):
    #return HttpResponse("Hello world")
    x=calculate()
    return render(request,'hello.html',{'name':'Suresh'})
