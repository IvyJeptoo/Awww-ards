from dataclasses import field
from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields=('title','category','link','description','image','pub_date','author')
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields=('user','photo','bio')
        
        