from django import forms
from . models import Profile,Product
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', )
class SizeForm(forms.ModelForm):
     class Meta:
        model = Product
        fields = ('size', )


# sending mail
class EmailPostForm(forms.Form):				
    name = forms.CharField(max_length=25)				
    email = forms.EmailField()
    to = forms.EmailField()								
    comments = forms.CharField(required=False, widget=forms.Textarea)
