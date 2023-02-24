
from django.shortcuts import render

def home(request):
    user = request.user
    return render(request,'base.html',{'user':user})

def product(request) :
    return render(request,'product.html')

def coa(request) :
    return render(request,'COA.html')
    
def coaDetail(request,pk) :
    return render(request,'COA_detail.html')

def productDetail(request,pk) :
    return render(request,'product_detail.html')

def incumbent(request) :
    return render(request,'incumbent.html')

def login(request) :
    return render(request,'login.html')

def register(request) :
    return render(request,'register.html')