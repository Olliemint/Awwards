from django.db import models

# Create your models here.

class Projectdata(models.Model):
    
    name = models.CharField(max_length=200, blank=False)
    posted_date = models.DateTimeField(auto_now_add=True)
    posted_by = models.CharField(max_length=200, blank=False)
    location = models.CharField(max_length=200, blank=False)
    project_link = models.URLField(max_length=500, blank=True)
    
    def __str__(self):
        return self.name
