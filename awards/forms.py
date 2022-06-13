from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]
        

class UpdateProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['photo', 'bio']
        
class PostProjectForm(forms.ModelForm):
    title = forms.CharField()
    category = forms.CharField()
    link =  forms.URLField()
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    

    class Meta:
        model = Profile
        fields = ['title', 'category','link','description','image']