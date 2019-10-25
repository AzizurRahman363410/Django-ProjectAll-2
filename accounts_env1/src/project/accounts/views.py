from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm,CustomloggedinForm

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            messages.success(request,f"Account created successfully!! Username is {username}")
            auth.login(request, user)
            return redirect("/registration/")
    else:
        form = CustomUserCreationForm()
    return render(request,'accounts/register.html', {'form':form})


def login(request):
    if request.method == 'POST':
        form = CustomloggedinForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, f"Account login successfully!!")
                return redirect('/registration/')
            else:
                messages.warning(request, f"Your Username or Password Doesn't match.")

    else:
        form = CustomloggedinForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth.logout(request)
    messages.info(request, f"Account LogOut successfully!!")
    return redirect('/registration/')
