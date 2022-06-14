
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(max_length=200, blank=True, null=True)
    country=models.CharField(max_length=200, blank=True, null=True)
    image=models.ImageField(default='user7.jpg',upload_to='projectpics')
    def __str__(self):
        return f'{self.user.username} Profile'
    
    
    def save_profile(self, **kwargs):
        super().save( **kwargs)
        img= Profile.open(self. profilepics.path)
    
    

class Projectdata(models.Model):
    author =models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=200, blank=False)
    posted_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200, blank=False)
    project_link = models.URLField(max_length=500, blank=False)
    project_image = models.ImageField(default='project.jpg',upload_to='projectpics')
    reviews = models.ManyToManyField(
    'Review', related_name='user_project', blank=True)
    
    
    def __str__(self):
        return self.name
    
   

    def delete_project(self):
        self.delete()

    @classmethod
    def search_projects(cls, search_term):
        found_data = cls.objects.filter(Q(name__icontains=search_term) | Q(author__username__icontains=search_term))
        return found_data
    @classmethod
    def posts(cls):
        return cls.objects.all()

    def save_project(self):
        self.save()
    
    
    
    
RATE_CHOICES =[
    (1, '1- Very Dissatisfied'),
    (2, '2- Dissatisfied'),
    (3, '3- bad'),
    (4, '4- OK'),
    (5, '5- neutral'),
    (6, '6- good'),
    (7, '7- very good'),
    (8, '8- Extremly good'),
    (9, '9- Perfect'),
    (10, '10 - Master Piece'),
 ]    
 
    
class Review(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Projectdata, on_delete=models.CASCADE) 
    review = models.CharField(max_length=2000, blank=True)
    design = models.PositiveSmallIntegerField(default=0, choices=RATE_CHOICES)
    usability = models.PositiveSmallIntegerField(default=0, choices=RATE_CHOICES)
    content = models.PositiveSmallIntegerField(default=0, choices=RATE_CHOICES)
    
    

    def __str__(self):
        return self.review
    
    
    
    def save_review(self):
        self.save()

    @classmethod
    def get_review(cls, id):
        ratings = cls.objects.filter(post_id=id).all()
        return ratings
