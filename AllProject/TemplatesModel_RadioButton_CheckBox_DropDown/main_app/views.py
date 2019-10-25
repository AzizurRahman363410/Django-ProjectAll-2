from django.shortcuts import render,redirect
from . forms import CustomPost
from . models import NewPost,Post
# Create your views here.
def home(request):
    form = CustomPost(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form':form
    }
    return render(request, 'home.html',context)
def display(request):
    new_post = NewPost.objects.all()
    context = {
        'new_post':new_post,
      
    }
    return render(request, 'display.html',context)