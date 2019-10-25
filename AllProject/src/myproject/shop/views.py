from django.shortcuts import render
from.models import Item,Order,OrderItem
from django.views.generic import DetailView, ListView , UpdateView
# Create your views here.

class HomeListView(ListView):
    model=Item
    template_name = 'shop/index.html'
  
def contact(request):
    return render(request,'shop/contact.html')
def about(request):
    return render(request,'shop/404.html')
def sale(request):
    return render(request,'shop/product.html')
def detail(request):
    return render(request,'shop/single.html')