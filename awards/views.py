
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *

# Create your views here.
class ProfileList(APIView):
    def get(self,request,format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile,many=True)
        return Response(serializers.data)
    
    
class ProjectList(APIView):
    def get(self,request,format=None):
        all_project = Project.objects.all()
        serializers = ProjectSerializer(all_project,many=True)
        return Response(serializers.data)
    

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
    category = request.GET.get('category')
    
    if category == None:
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(category__name = category)
        
        
    
    projects = Project.projects()
    context = {
        # 'projects': projects,
        
        'projects': projects
        }
    return render(request, 'main/project.html', context)

def postProject(request): 
    
    if request.method == 'POST':
        form = PostProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user.profile
            project.save()
            print(project)
        return redirect(to='project')
        
        
    
    else:
        form = PostProjectForm()
    context ={
        'form': form,
            
    }
        
    return render(request, 'main/post_project.html',context)
    
    


@login_required
def viewProfile(request):  
    projects = request.user.profile.projects.all()    
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if profile_form.is_valid():  
            profile = profile_form.save(commit=False)
            profile.author = request.user.profile          
            profile.save()
        # return redirect (to='viewProfile')
            return HttpResponseRedirect(request.path_info)    
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)
        context = {
            'profile_form': profile_form,
            'projects':projects
        }        
    return render(request, 'main/view_profile.html',context)



def searchProject(request):
    if 'search-project' in request.GET and request.GET['search-project']:
        name = request.GET.get('search-project')
        results = Project.search_project_by_category(name)
        message = name
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'main/results.html', params)
    else:
        message = 'You did not make any selection'
    return render(request, 'main/results.html', {'message': message})
    



