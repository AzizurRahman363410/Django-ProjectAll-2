from django import forms
from . models import ModelFormOne

# must need for creat user other wise password1 , amd password2 will not create
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomFormOne(forms.ModelForm):

    class Meta:
        model = ModelFormOne
        fields = ['title', 'image']

class CustomFormTwo(forms.Form):
    heading = forms.CharField(max_length=300)
    image = forms.ImageField()



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class CustomloggedinForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
