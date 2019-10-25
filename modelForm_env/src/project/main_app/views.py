from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomFormOne, CustomFormTwo, SignUpForm,CustomloggedinForm
from . models import ModelFormOne,ModelFormTwo


# Create your views here.
def home(request):
    return render(request, 'main_app/home.html')


def formOne(request):
    if request.method == 'POST':
        form = CustomFormOne(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CustomFormOne()
    return render(request, 'main_app/formOne.html', {'form': form})


# form two normal form
def formTwo(request):
    if request.method == 'POST':
        form = CustomFormTwo(request.POST, request.FILES)
        if form.is_valid():


            # heading = form.cleaned_data.get('heading')
            # image = form.cleaned_data.get('image')
            # formTwo = ModelFormTwo(heading=heading,image=image)
            # formTwo.save()


            formTwo = ModelFormTwo()
            formTwo.heading = form.cleaned_data.get('heading')
            formTwo.image = form.cleaned_data.get('image')
            formTwo.save()

            return redirect('/')
    else:
        form = CustomFormTwo()
    return render(request, 'main_app/formTwo.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # for login
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'main_app/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = CustomloggedinForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            auth.login(request, user)
            return redirect('/')
    else:
        print('two')
        form = CustomloggedinForm()
    context = {
        'form':form
    }
    return render(request, 'main_app/login.html', context)