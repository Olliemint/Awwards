from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.Register, name='register'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('review/<str:id>/',views.ReviewView, name='review'),
    path('submit/',views.Submit_site,name='submit'),
    path('profile/',views.Profile,name='profile'),
    path('search/',views.Search_projects,name='search'),
    
    
    
    
]