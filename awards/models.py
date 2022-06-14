
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

# from django_countries.fields import CountryField

CATEGORIES = (
    ('Python','Python'),
    ('Java','Java'),
    ('Angular','Angular'),
    ('Flask','Flask'),
    ('Ruby','Ruby')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    photo = CloudinaryField('image',default='http://res.cloudinary.com/dim8pysls/image/upload/v1639001486/x3mgnqmbi73lten4ewzv.png')
    bio = models.CharField(max_length=300) 
    
    
    # def save_profile(self):
    #     self.save()  
        
    def delete_profile(self):
        self.delete()      
        
    
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
            
            
    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
        
    def __str__(self):
        return self.bio
    
   
    

    
class Project(models.Model):    
    title = models.CharField(max_length=300,blank=False)
    author = models.ForeignKey('Profile',on_delete=models.CASCADE,related_name='projects')
    category = models.CharField( max_length=15, choices=CATEGORIES, default=1)
    link = models.URLField(blank=False)
    description = models.TextField(blank=False)
    image = CloudinaryField('image')
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    # country = CountryField(blank_label='(select country)', default='KE')
    
    
    @classmethod
    def get_by_author(cls, author):
        projects = cls.objects.filter(author=author)
        return projects
    
    @classmethod
    def projects(cls):
        projects = cls.objects.all()
        return projects
    
    @classmethod
    def get_project(request, id):
        try:
            project = Project.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return project    
    
    
    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()       
        
    
        
    @classmethod    
    def get_projects(cls):
        projects = cls.objects.all()
        return projects
    
    @classmethod
    def search_project_by_category(cls, category):
        projects = cls.objects.filter(category__icontains=category)
        return projects
    
    def __str__(self):
        return self.title
    
    
    
    
    
    
    
    
       
    
    
    
    
    
    
   
 