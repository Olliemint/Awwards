from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProjectSerializer
from .models import Projectdata
import requests

# Create your views here.
class ProjectView(viewsets.ModelViewSet):
    queryset = Projectdata.objects.all()
    serializer_class = ProjectSerializer



def home(request):
    response_json = requests.get('http://127.0.0.1:8000/api/project/') 
    if (response_json.status_code == 200):  
        response = response_json.json() 
    context = {
        'response': response
    }    
    
    return render(request, 'awwards/home.html',context)



def Login(request):
    
    return render(request, 'awwards/login.html')


def Logout(request):
    
    return render(request, 'awwards/logout.html')
