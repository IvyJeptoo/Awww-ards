from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

# from django_countries.fields import CountryField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    photo = CloudinaryField('image',default='http://res.cloudinary.com/dim8pysls/image/upload/v1639001486/x3mgnqmbi73lten4ewzv.png')
    bio = models.CharField(max_length=300) 
    
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            
            
    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    @classmethod
    def profile(cls):
        profiles = cls.objects.all()
        return profiles

    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def save_profile(self):
        self.user

    def __str__(self):
        return self.bio

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all() 
    
    

    def delete_profile(self):
        self.delete()
        
    @classmethod
    def update_profile(cls, profile):
        category = cls.get_profile_by_id(profile.id)
        category.name = profile.name
        category.save_profile()
        

    
    
    
class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)
    
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
        
        
    @classmethod
    def update_category(cls, cat):
        category = cls.get_category_by_id(cat.id)
        category.name = cat.name
        category.save_category()
        
    @classmethod
    def get_category_by_id(cls, id):
        category = cls.objects.get(id=id)
        return category
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=300,blank=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    link = models.URLField(blank=False)
    description = models.TextField(blank=False)
    image = CloudinaryField('image')
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    # country = CountryField(blank_label='(select country)', default='KE')
    
    
    @classmethod
    def get_by_author(cls, author):
        projects = cls.objects.filter(author=author)
        return projects
    
    
    
    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()
        
        
    @classmethod
    def update_project(cls, project):
        category = cls.get_project_by_id(project.id)
        category.name = project.name
        category.save_project()
        
    @classmethod    
    def get_projects(cls):
        projects = cls.objects.all()
        return projects
    
    def __str__(self):
        return self.title
    
    
    
    
    
    
    
    
       
    
    
    
    
    
    
   
 