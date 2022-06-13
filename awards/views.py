from django.shortcuts import render
from .forms import RegisterForm
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

def viewProfile(request):
    return render(request, 'main/view_profile.html')

def editProfile(request):
    return render(request, 'main/edit_profile.html')

