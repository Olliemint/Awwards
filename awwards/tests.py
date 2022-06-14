from django.test import TestCase
from .models import Profile, Projectdata,Review,password
from django.contrib.auth.models import User

# Create your tests here.
class TestReview(TestCase):
    def setUp(self):
        self.project = Projectdata(author= User.objects.create(username='Olliemint'),name='Akan Names',  location='Nairobi', project_link='http://akanify.herokuapp.com', project_image='test.jpg',)
        self.user = User( username='Olliemint', password='@test.password')
        self.rating = Review.objects.create(design=6, usability=7, content=9, user=self.user)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Review))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Review.objects.all()
        self.assertTrue(len(rating) > 0)





class TestProfile(TestCase):
    
    def setUp(self):
        self.user = User(username='Olliemint',bio='test bio', country='Kenya',image='profile.jpg')
        self.user.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save_profile()

class TestProject(TestCase):
    def setUp(self):
        self.project = Projectdata(author= User.objects.create(username='Olliemint'),name='Akan Names',  location='Nairobi', project_link='http://akanify.herokuapp.com', project_image='test.jpg',)
        self.user = User(username='Olliemint', password='@test.password')

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Projectdata))

    def test_save(self):
        self.project.save()
        project = Projectdata.objects.all()
        self.assertTrue(len(project) > 0)

    def test_get_project(self):
        self.project.save()
        project = Projectdata.project()
        self.assertTrue(len(project) > 0)

    def test_search_post(self):
        self.project.save()
        project = Projectdata.search_projects('test')
        self.assertFalse(len(project) > 0)

