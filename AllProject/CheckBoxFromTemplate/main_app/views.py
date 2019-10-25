from django.shortcuts import render,redirect
from . models import Post
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # checkbox = request.POST.get('checkbox',False)
        checkbox = request.POST.get('checkbox','off') 
        if(checkbox == 'on'):
            post = Post.objects.create(email=email,password=password)
            post.save()
        else:
           messages.info(request, 'Please Check Trams and Conditions.')
           return redirect('/')
    return render(request, 'home.html')