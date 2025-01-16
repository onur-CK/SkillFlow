from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Service, Availability, Appointment, WeeklySchedule

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
        # Django Html Attr Source: https://www.geeksforgeeks.org/how-to-add-html-attributes-to-input-fields-in-django-forms/
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control custom-input',
                'placeholder': 'e.g, Professional Math Tutoring'
            }),
            # Django Text-area Html Attr Source: https://stackoverflow.com/questions/66707030/django-textarea-form
            'description': forms.Textarea(attrs={
                'class': 'form-control custom-input',
                'rows': 4,
                'maxlength': 500,
                'placeholder': 'Describe your service, experience, and expertise...'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control custom-input'
            }),
            # Min Attr Source: https://stackoverflow.com/questions/37024650/specify-max-and-min-in-numberinput-widget
            'hourly_rate': forms.NumberInput(attrs={
                'class': 'form-control custom-input',
                'placeholder': 'Enter your hourly rate',
                'min': '1'
            })
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['availability']


class WeeklyScheduleForm(forms.ModelForm):
    class Meta:
        model = WeeklySchedule
        fields = ['day_of_week', 'start_time', 'end_time', 'location']
        widgets = {
            'day_of_week': forms.Select(attrs={
                'class': 'form-control custom-input'
            }),
            'start_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control custom-input'
            }),
            'end_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control custom-input'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control custom-input',
                'placeholder': 'Enter meeting location'
            })
        }