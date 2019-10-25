from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'accounts/home.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f" You are successfully SignUp")


            # for login
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, f" You are login successfully ")

                return redirect('accounts:login')
            else:
                messages.warning(request, f"Your Username or Password Doesn't match.")

    else:
        form = AuthenticationForm()
        print('Four')

        return render(request, 'accounts/login.html',{'form': form})
def logout(request):
    auth.logout(request)
    messages.success(request, f" You are successfully Logout")
    return redirect('accounts:login')