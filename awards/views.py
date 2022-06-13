from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
           
            form.save()
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})

def home(request):
    return render(request, 'main/home.html')

def project(request):
    return render(request, 'main/project.html')

def postProject(request):
    return render(request, 'main/post_project.html')


@login_required
def viewProfile(request):    
       
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if profile_form.is_valid():            
            profile_form.save()
        return redirect (to='viewProfile')
    
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)
        context = {
            'profile_form': profile_form
        }
        
    return render(request, 'main/view_profile.html',context)

