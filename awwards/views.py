from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



from .forms import RegisterUserForm,ReviewForm
from django.contrib import messages


from django.shortcuts import render,redirect
from rest_framework import viewsets
from .serializers import ProjectSerializer
from .models import Projectdata,Review
from django.db.models import Q
import requests
from django.db.models import Avg


# Create your views here.

class ProjectView(viewsets.ModelViewSet):
    queryset = Projectdata.objects.all()
    serializer_class = ProjectSerializer


# home view
def home(request):
    
    
    projects = Projectdata.objects.all()
    response_json = requests.get('http://127.0.0.1:8000/api/project/') 
    if (response_json.status_code == 200):  
        response = response_json.json() 
    context = {
        
        'projects': projects,
        
    }    
    
    return render(request, 'awwards/home.html',context)


def post(request):
    
    return render(request, 'logout.html',)


# user registration view

def Register(request):
    if request.user.is_authenticated:
        
        return redirect('home')
    # Do something for authenticated users.
  
    else:
    # Do something for anonymous users.
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


# login view
def Login(request):
    if request.user.is_authenticated:
        
        return redirect('home')
    # Do something for authenticated users.
    
    else:
    # Do something for anonymous users.
    
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

# logout view
def Logout(request):
    
    logout(request)
    
    return redirect('home')


# review view
@login_required(login_url='login')
def ReviewView(request,id):
    
    form = ReviewForm()
    
    project = Projectdata.objects.get(id=id)
    user  = request.user
    reviews = Review.objects.get(project_id=id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = user
            data.project = project
            data.save()
            
           
            return HttpResponse('Thank you for your feedback')
    
    context = {
        'project':project,
        'form':form,
        'reviews':reviews,
    }
    
    
    
    return render(request, 'awwards/review.html',context)



@login_required(login_url='login')

def Submit_site(request):
    
    if request.method == 'POST':
        
        name = request.POST.get('projectname')
        location = request.POST.get('location')
        project_link = request.POST.get('plink')
        project_image = request.FILES.get('upload')
        
        author = request.user
        
        post = Projectdata.objects.create(
            author=author,name=name,location=location,project_link=project_link,project_image=project_image
        )
        return redirect('home')
    
    
    return render(request, 'awwards/submit_site.html')


