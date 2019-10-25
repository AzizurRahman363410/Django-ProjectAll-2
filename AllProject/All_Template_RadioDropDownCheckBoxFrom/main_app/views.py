from django.shortcuts import render,redirect
from . models import Post
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        dropdown = request.POST['dropdown']
        gender = request.POST['gender']
        sports = request.POST.getlist('sports')  #for Checkbox as if its a list so write getlist
       
        checkbox = request.POST.get('checkbox','off') 

        if(checkbox == 'on'):
            post = Post.objects.create(email=email,password=password,dropdown=dropdown,gender=gender,sports=sports)
            post.save()
        else:
           messages.info(request, 'Please Check Trams and Conditions.')
           return redirect('/')
    return render(request, 'home.html')