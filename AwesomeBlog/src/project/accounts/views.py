from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth import authenticate
from . models import Profile

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f" Account created for: {username}")
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/registration.html', {'form': form})

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
                return redirect('/')
        else:
            messages.warning(request, f"Your Username or Password Doesn't match.")
            return redirect('accounts:login')

    else:
        form = AuthenticationForm()
        return render(request,'accounts/login.html',{'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, f" You are Logout successfully ")
    return redirect('accounts:login')

# ...................................
def load_profile(user):
  try:
    return user.profile
  except:  # this is not great, but trying to keep it simple
    profile = Profile.objects.create(user=user)
    return profile




def editprofile(request):
    profile = load_profile(request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(
            instance=request.user,
            data=request.POST,
        )
        p_form = ProfileUpdateForm(
            instance=profile,
            data=request.POST,
            files=request.FILES,
        )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f" Profile are successfully updated ")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/editprofile.html',context)




