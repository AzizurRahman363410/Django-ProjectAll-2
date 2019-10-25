from django.shortcuts import render,get_object_or_404
from .models import Book
from django.views.generic import ListView,DetailView


# using class ..............................
class HomePageView(ListView):
    model = Book
    context_object_name = 'book_lists'
#  also you ca used instead of book_lists , book_list  OR object_list

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
#  also you ca used instead of book , use object
