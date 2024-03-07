from django.shortcuts import render
from .models import product,cartitems

def home(request):
    prod = product.objects.all()
    return render(request,'index.html',{'prod':prod})

def cart(request):
    cart = cartitems.objects.all()
    return render(request,'cart.html',{'cart':cart})
