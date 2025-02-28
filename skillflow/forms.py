from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import (
    UserProfile,
    Service,
    Availability,
    Appointment,
    WeeklySchedule
)
from django.utils import timezone

# This module contains all form classes used in the SkillFlow application.
# Forms handle data validation and provide HTML rendering of form fields.


class SignUpForm(UserCreationForm):
    """
    Form for user registration.
    Inherits from Django's UserCreationForm
    to handle user creation with password validation.
    """
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 20:
            raise forms.ValidationError('Username must be 20 characters or fewer.')
        return username
        

class UserProfileForm(forms.ModelForm):
    """
    Form for managing user profile information.
    Allows users to update their personal information including
    name, email, and bio.
    """
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "email", "bio"]
        widget = {
            # Configures the bio field as a textarea with specific attributes
            "bio": forms.Textarea(attrs={"rows": 4, "maxlength": 200}),
        }


class ServiceForm(forms.ModelForm):
    # Form for creating and editing service listings.
    # Includes custom widget configurations for improved user experience.
    class Meta:
        model = Service
        fields = ["title", "description", "category", "hourly_rate"]
        # https://www.geeksforgeeks.org/how-to-add-html-attributes-to-input-fields-in-django-forms/
        widgets = {
            # Custom styling and placeholders for each field
            "title": forms.TextInput(
                attrs={
                    "class": "form-control custom-input",
                    "placeholder": "e.g, Professional Math Tutoring",
                }
            ),
            # https://stackoverflow.com/questions/66707030/django-textarea-form
            "description": forms.Textarea(
                attrs={
                    "class": "form-control custom-input",
                    "rows": 4,
                    "maxlength": 500,
                    "placeholder": (
                        "Describe your service, "
                        "experience, and expertise..."
                    ),
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-control custom-input"
                }
            ),
            # https://stackoverflow.com/questions/37024650/specify-max-and-min-in-numberinput-widget
            "hourly_rate": forms.NumberInput(
                attrs={
                    "class": "form-control custom-input",
                    "placeholder": (
                        "Enter your hourly rate"
                    ),
                    "min": "1",
                    "max": "9999.99",
                }
            ),
        }

    def clean_hourly_rate(self):
        hourly_rate = self.cleaned_data.get("hourly_rate")
        if hourly_rate and hourly_rate < 0:
            raise forms.ValidationError("Hourly rate cannot be negative.")
        return hourly_rate


class AvailabilityForm(forms.ModelForm):
    """
    Form for managing service provider availability.
    Includes custom field definitions and
    validation logic for dates and times.
    """

    # Custom field definitions with specific widget configurations
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control custom-input",
                # https://docs.djangoproject.com/en/5.1/topics/i18n/timezones/
                # Prevents past dates
                "min": timezone.now().date().isoformat(),
            }
        )
    )

    start_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={"type": "time", "class": "form-control custom-input"}
        )
    )

    end_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={"type": "time", "class": "form-control custom-input"}
        )
    )

    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control custom-input",
                "placeholder": "Enter meeting location",
            }
        )
    )

    class Meta:
        model = Availability
        fields = ["date", "start_time", "end_time", "location"]

    # https://docs.djangoproject.com/en/5.1/ref/forms/validation/
    def clean(self):
        # Custom validation method to ensure:
        # 1. Date is not in the past
        # 2. End time is after start time
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        # https://docs.djangoproject.com/en/5.1/ref/forms/validation/
        if date and date < timezone.now().date():
            raise forms.ValidationError(
                "Cannot create availability for past dates"
                )

        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError("End time must be after start time")

        return cleaned_data


# Form for handling appointment creation and management.
# Provides a simple interface for selecting available time slots.
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "availability"
        ]  # Only the availability field is exposed for selection


class WeeklyScheduleForm(forms.ModelForm):
    class Meta:
        model = WeeklySchedule
        fields = ["day_of_week",
                  "start_time",
                  "end_time",
                  "location"]
        widgets = {
            "day_of_week": forms.Select(
                attrs={
                    "class": "form-control custom-input"
                }
            ),
            "start_time": forms.TimeInput(
                attrs={"type": "time", "class": "form-control custom-input"}
            ),
            "end_time": forms.TimeInput(
                attrs={"type": "time", "class": "form-control custom-input"}
            ),
            "location": forms.TextInput(
                attrs={
                    "class": "form-control custom-input",
                    "placeholder": "Enter meeting location",
                }
            ),
        }
