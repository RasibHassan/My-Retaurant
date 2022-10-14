# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    print('sdas')
    return HttpResponse('<a href="/shop"><h1>lets goo!! <h2></a>')
        