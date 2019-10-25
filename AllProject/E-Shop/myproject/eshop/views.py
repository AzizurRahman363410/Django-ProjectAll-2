from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'eshop/index.html');

def contact(request):
    return render(request, 'eshop/contact.html');
def about(request):
    return render(request, 'eshop/about.html');

def register(request):
    return render(request, 'eshop/register.html');
def login(request):
    return render(request, 'eshop/account.html');
def checkout(request):
    return render(request, 'eshop/checkout.html');
def productList(request):
    return render(request, 'eshop/products.html');
def detail(request):
    return render(request, 'eshop/single.html');