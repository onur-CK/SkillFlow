from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Service

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'bio']
        widget = {
            'bio': forms.Textarea(attrs={'rows': 4, 'maxlength': 200}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'category', 'hourly_rate']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control custom-input',
                'placeholder': 'e.g, Professional Math Tutoring'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control custom-input',
                'rows': 4,
                'maxlength': 500,
                'placeholder': 'Describe your service, experience, and expertise...'
            })
        }

