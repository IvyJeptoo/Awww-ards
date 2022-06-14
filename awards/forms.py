from wsgiref.validate import validator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile,Project



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
    # title = forms.CharField()
    # category = forms.ChoiceField( choices=CHOICES)
    # link =  forms.URLField()
    # description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    # image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    

    class Meta:
        model = Project
        exclude=['author','pub_date']