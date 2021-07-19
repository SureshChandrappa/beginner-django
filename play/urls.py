from django.urls import path
from . import views

urlpatterns=[
    path('hello/',views.sya_hello)
]