from django.shortcuts import render
from .models import product

def home(request):
    prod = product.objects.all()
    return render(request,'index.html',{'prod':prod})
