
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Projectdata(models.Model):
    
    name = models.CharField(max_length=200, blank=False)
    posted_date = models.DateTimeField(auto_now_add=True)
    posted_by = models.CharField(max_length=200, blank=False)
    location = models.CharField(max_length=200, blank=False)
    project_link = models.URLField(max_length=500, blank=False)
    project_image = models.ImageField(default='project.jpg',upload_to='projectpics')
    reviews = models.ManyToManyField(
    'Review', related_name='user_project', blank=True)
    
    
    def __str__(self):
        return self.name
    
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
      
