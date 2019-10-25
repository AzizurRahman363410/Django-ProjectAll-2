from django.shortcuts import render,get_object_or_404
from .models import Book
# Create your views here.
def index(request):
    context = {
        'book_lists':Book.objects.all()
    }
    return render(request,"book/index.html",context)

def details(request,id):
    context = {
        # 'book':Book.objects.get(pk=id)
        # 'book':Book.objects.get(id=id)
        'book':get_object_or_404(Book,pk=id)
        # 'book':get_object_or_404(Book,id=id)
    }
    return render(request,"book/details.html",context)