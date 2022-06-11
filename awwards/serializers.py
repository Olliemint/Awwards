from pyexpat import model
from rest_framework import serializers
from .models import Projectdata


class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Projectdata
        
        fields = ['name', 'posted_date', 'posted_by', 'location' ,'project_link']

