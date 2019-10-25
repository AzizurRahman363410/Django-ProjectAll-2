from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from .models import Book
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView

# remember crate a folder as your apps name, this project my apps name is
# book so all the html file i keep in templates/book/base.html or book_list.html
# using class ..............................
class HomePageView(ListView):
    model = Book
#  also you ca used instead of book_lists , book_list  OR object_list

class BookDetailView(DetailView):
    model = Book
#  also you ca used instead of book , object


# search
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        # search_result = Book.objects.filter(title__icontains=search_term)

        # For complex Query for search

        search_result = Book.objects.filter(
        Q(title__icontains=search_term) |
        Q(desc__icontains=search_term) |
        Q(publisher__icontains=search_term)
        )

        context = {
                'search_term':search_term,
                'book_list': search_result
            }
        return render(request,"book/search.html",context)
    else:
        return redirect('book:home')

class BookCreateView(CreateView):
    model = Book
    fields = ['title','authors','desc','publisher','image','publication_date']
    template_name = "book/create.html"
    success_url = '/'

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title','authors','desc','publisher','image','publication_date']
    template_name = "book/update.html"
    success_url = '/'
class BookDeleteView(DeleteView):
    model = Book
    context_object_name = 'item'
    template_name = "book/delete.html"
    success_url = '/'