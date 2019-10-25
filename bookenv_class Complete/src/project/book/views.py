from django.shortcuts import render,get_object_or_404
from .models import Book
from django.views.generic import ListView,DetailView

# remember crate a folder as your apps name, this project my apps name is
# book so all the html file i keep in templates/book/base.html or book_list.html
# using class ..............................
class HomePageView(ListView):
    model = Book
#  also you ca used instead of book_lists , book_list  OR object_list

class BookDetailView(DetailView):
    model = Book
#  also you ca used instead of book , object
