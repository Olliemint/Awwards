
from rest_framework import serializers
from .models import Projectdata,Profile
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):
    project_image = serializers.ImageField(max_length=None,use_url=True)
    
    class Meta:
        model = Projectdata
        
        fields = ['id','name', 'posted_date', 'location' ,'project_link', 'project_image']
        
        
class ProfileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,use_url=True)
    
    class Meta:
        model = Profile
        
        fields = ['bio', 'country', 'image']
        
        

class UserSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(read_only=True)
  project = ProjectSerializer(read_only=True, many=True)

  class Meta:
    model = User
    fields = ['id', 'url', 'username', 'profile', 'project']                

