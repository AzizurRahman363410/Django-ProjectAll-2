from django.core.mail import send_mail
from django.shortcuts import render,get_object_or_404,redirect
from . models import Product,Profile
from . forms import UserForm,ProfileForm,SizeForm,EmailPostForm
from django.views.generic import CreateView
from django.contrib import messages
from django.conf import settings
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = SizeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SizeForm()
    all_prods = Product.objects.all()
    context = {
        'all_prods': all_prods,
        'form':  form
    }
    return render(request, 'home.html',context)
def detail(request,slug):
    context = {
        'product_list': get_object_or_404(Product, slug=slug)
    }
    return render(request, 'detail.html',context)


def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST or None)
        profile_form = ProfileForm(request.POST or None)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            phone = profile_form.cleaned_data['phone']
            profile_create = Profile.objects.create(user=request.user, phone=phone)
            profile_create.save()
            messages.success(request,('Your profile was successfully updated!'))
            return redirect('home')
        else:
            return render(request,'profile.html')
    else:
        profile_form = ProfileForm()
        user_form = UserForm()
    return render(request, 'profile.html', {
        'profile_form': profile_form,
        'user_form' : user_form,
    })


def send_email(request): 
    if	request.method == 'POST':
        form = EmailPostForm(request.POST or None)
        if form.is_valid():
            cd = form.cleaned_data
            subject = "Hello {}".format(cd['name'])
            message = 'please check your confirmation message  '
            recipient_list = cd['to']
            from_email = settings.EMAIL_HOST_USER
            # send_mail('subject', 'body of the message', 'azizur.rahman363410@gmail.com', ['shakil.ahmed363410@gmail.com',],fail_silently=False)
            
            send_mail(subject, message, from_email, [recipient_list], fail_silently=False,)
            return redirect('home')
    else:
        form = EmailPostForm()
        return render(request, 'sendingmail.html',	{'form':form})
  
