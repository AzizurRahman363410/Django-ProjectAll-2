from django.db.models import Q
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils import timezone
from django.core.paginator import Paginator
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Blog
# Create your views here.
def home(request):
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 6)  # Show 25 contacts per page

    page = request.GET.get('page')
    blog = paginator.get_page(page)

    context = {
        'blog_list':blog
    }
    return render(request,"blog/blog_list.html",context)


def detail(request,id):
    context = {
        'blog':get_object_or_404(Blog,pk=id)
    }
    return render(request,"blog/blog_detail.html",context)


@login_required(login_url='/accounts/login/')
def create_product(request):
    if request.method == 'POST':
        if request.POST['title'] and request.FILES['image'] and request.POST['description']:
            blog=Blog()
            blog.title = request.POST['title']
            blog.image = request.FILES['image']
            blog.description = request.POST['description']
            # blog.pub_date = timezone.datetime.now()
            blog.author = request.user
            blog.save()
            return redirect('/blog/')
        else:
            return render(request, "blog/create_product.html",{'error':'Please fill all the fields'})
    else:
        return render(request, "blog/create_product.html")


    return render(request,"blog/create_product.html")


def search(request):
    if request.method == 'POST':
        if request.POST['search_term']:
            search_term = request.POST['search_term']
            # search_result = Book.objects.filter(title__icontains=search_term)

            search_result = Blog.objects.filter(
                Q(title__icontains=search_term) |
                Q(description__icontains=search_term)
                # Q(author__icontains=search_term)
            )

            context = {
                'search_term': search_term,
                'blog_list': search_result,
            }
            return render(request, "blog/search.html", context)
        else:
            return render(request, "blog/search.html")
    else:
        return render(request,'blog/blog_list.html')

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog/delete.html"
    context_object_name = 'blog'
    success_url = '/blog/'

class BookUpdateView(UpdateView):
    model = Blog
    fields = ['image', 'title', 'description', 'author']
    template_name = "blog/update.html"
    success_url = reverse_lazy('blog:home')