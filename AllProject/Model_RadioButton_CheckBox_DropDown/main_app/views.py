from django.shortcuts import render,redirect
from . forms import CustomPost
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