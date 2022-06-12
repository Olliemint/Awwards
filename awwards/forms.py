from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review,RATE_CHOICES

from django import forms

class RegisterUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']
        
        
class ReviewForm(forms.ModelForm):
    
    review = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),required=True)
    design = forms.ChoiceField(choices=RATE_CHOICES, widget= forms.Select(),required=True)
    usability = forms.ChoiceField(choices=RATE_CHOICES, widget= forms.Select(),required=True)
    content = forms.ChoiceField(choices=RATE_CHOICES, widget= forms.Select(),required=True)


    
    class Meta:
        model = Review
        fields = ['review', 'design','usability','content']
            
    
    
