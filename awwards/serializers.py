
from rest_framework import serializers
from .models import Projectdata


class ProjectSerializer(serializers.ModelSerializer):
    project_image = serializers.ImageField(max_length=None,use_url=True)
    
    class Meta:
        model = Projectdata
        
        fields = ['id','name', 'posted_date', 'location' ,'project_link', 'project_image']

