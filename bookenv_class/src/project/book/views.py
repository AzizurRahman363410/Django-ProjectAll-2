from django.shortcuts import render,get_object_or_404
from .models import Book
from django.views.generic import ListView,DetailView
# Create your views here.


# using method ..............................
# def index(request):
#     context = {
#         'book_lists':Book.objects.all()
#     }
#     return render(request,"book/index.html",context)

# using class ..............................
class HomePageView(ListView):
    template_name = 'book/index.html'
    model = Book
    context_object_name = 'book_lists'




# def details(request,id):
#     context = {
#         # 'book':Book.objects.get(pk=id)
#         # 'book':Book.objects.get(id=id)
#         'book':get_object_or_404(Book,pk=id)
#         # 'book':get_object_or_404(Book,id=id)
#     }
#     return render(request,"book/details.html",context)
#
class BookDetailView(DetailView):
    template_name = 'book/details.html'
    model = Book
    context_object_name = 'book'

