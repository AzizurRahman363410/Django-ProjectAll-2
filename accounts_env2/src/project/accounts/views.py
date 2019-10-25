from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.shortcuts import render,redirect
from .forms import SignUpForm,CustomloggedinForm
# Create your views here.
def home(request):
    return render(request,'accounts/home.html')
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()


            # for login
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomloggedinForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password,email=email)
            auth.login(request, user)
            return redirect('/')
    else:
        form = CustomloggedinForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)
