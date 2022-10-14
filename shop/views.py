# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import product
from math import ceil
from .models import *


def index(request):
    return render(request,'shop/index.html')

def menu(request):
    products= product.objects.all()
    allProds=[]
    catprods= product.objects.values('sub_category', 'id')
    print(catprods)
    cats= {item["sub_category"] for item in catprods}
    cats=list(cats)
    cats.remove('drink')
    cats.append('drink')
    for cat in cats:
        prod=product.objects.filter(sub_category=cat)
        n = len(prod)
        
        
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
        params={'allProds':allProds ,'responsive':1}
    return render(request,"shop/menu.html", params)
    
def about(request):
    return render(request,'shop/about.html')
def Contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contacts = contact(name=name, email=email, phone=phone, desc=desc)
        contacts.save()
        thank = 'true'
        return render(request, 'shop/contact.html', {'thank':thank,})

    return render(request, "shop/contact.html")


    


def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        order_id = '2022-'+str(order.order_id)
        print(order_id)
        thank = 'true'
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': order_id})
    return render(request, 'shop/checkout.html')
        