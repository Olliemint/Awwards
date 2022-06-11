from django.contrib.auth import authenticate,login,logout
from .forms import RegisterUserForm
from django.contrib import messages


from django.shortcuts import render,redirect
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


def Register(request):
    
    
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
        
        
    
    
    
    context = {
        'form': form,
    }
    
    return render(request, 'awwards/register.html',context)



def Login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('home')
        else:
            messages.warning(request, 'Username or password is incorrect')
    
    return render(request, 'awwards/login.html')


def Logout(request):
    
    logout(request)
    
    return redirect('home')
