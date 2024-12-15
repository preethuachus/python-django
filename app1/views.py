from django.shortcuts import render
from app1.models import contact,shipping
# Create your views here.
def index1(request):
    return render(request,"index.html")

def story(request):
    return render(request,"about.html")

def products(request):
    return render(request,"products.html")

def faq(request):
    return render(request,"faq.html")

def contact(request):
    return render(request,"contact.html")

def sign_in(request):
    return render(request,"sign-in.html")

def sign_up(request):
    return render(request,"sign-up.html")


def contactpage(request):
    if request.method=="POST":
        e=contact()
        e.name=request.POST.get("name")
        e.email=request.POST.get("email")
        e.subject=request.POST.get("subject")
        e.message=request.POST.get("message")
        e.save()
        return render(request,"contact.html")

def shipping(request):
    if request.method=="POST":
        b=shipping()
        b.email=request.POST.get("email")
        b.password=request.POST.get("password")
        b.save()
        return render(request,"sign-in.html")


def product_detail(request):
    return render(request,"product-detail.html")

