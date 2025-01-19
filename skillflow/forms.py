from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Service, Availability, Appointment, WeeklySchedule
from django.utils import timezone

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

class AvailabilityForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control custom-input',
            # Timezone Source Code: https://docs.djangoproject.com/en/5.1/topics/i18n/timezones/
            'min': timezone.now().date().isoformat()
        })
    )
    
    start_time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control custom-input'
        })
    )
    
    end_time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control custom-input'
        })
    )
    
    location = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control custom-input',
            'placeholder': 'Enter meeting location'
        })
    )

    class Meta:
        model = Availability
        fields = ['date', 'start_time', 'end_time', 'location']

    # Source Link: https://docs.djangoproject.com/en/5.1/ref/forms/validation/
    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        # Source Link: https://docs.djangoproject.com/en/5.1/ref/forms/validation/
        if date and date < timezone.now().date():
            raise forms.ValidationError("Cannot create availability for past dates")

        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError("End time must be after start time")

        return cleaned_data


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