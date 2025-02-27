from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .forms import SignUpForm, UserProfileForm, ServiceForm, AvailabilityForm

"""
Source Links for Django Form Testing:
- https://docs.djangoproject.com/en/5.0/topics/testing/tools/#form-testing
- https://docs.djangoproject.com/en/5.0/ref/forms/validation/
- https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#field-validation
"""


class SignUpFormTests(TestCase):
    """
    Test suite for user registration form validation.
    Tests both valid and invalid form submissions to ensure proper validation.
    """

    def test_signup_form_valid_data(self):
        """
        Test that the signup form accepts valid registration data.
        Ensures form validates successfully with correct username and matching passwords.
        """
        form_data = {
            "username": "testuser",
            "password1": "TestPass123!",
            "password2": "TestPass123!",
        }
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_signup_form_invalid_data(self):
        """
        Test that the signup form properly rejects invalid registration data.
        Specifically tests password mismatch scenario.
        """
        # Source Link: https://stackoverflow.com/questions/21458387/how-to-test-django-form-validation
        form_data = {
            "username": "testuser",
            "password1": "TestPass123!",
            "password2": "DifferentPass123!",
        }
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn(
            "password2", form.errors
        )  # Ensures error is related to password mismatch


class UserProfileFormTests(TestCase):
    """
    Test suite for user profile form validation.
    Verifies proper handling of profile information updates.
    """

    def test_profile_form_valid_data(self):
        """
        Test that the profile form accepts valid profile data.
        Verifies all profile fields can be properly updated.
        """
        form_data = {
            "first_name": "Test",
            "last_name": "User",
            "email": "test@example.com",
            "bio": "Test bio",
        }
        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_profile_form_bio_length(self):
        """
        Test that the profile form enforces maximum bio length.
        Ensures bio text cannot exceed 200 characters.
        """
        # Source Link: https://docs.djangoproject.com/en/5.0/ref/validators/#maxlengthvalidator
        long_bio = "x" * 201  # Create bio text that exceeds max length
        form_data = {
            "first_name": "Test",
            "last_name": "User",
            "email": "test@example.com",
            "bio": long_bio,
        }
        form = UserProfileForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("bio", form.errors)  # Verifies error is related to bio field


class ServiceFormTests(TestCase):
    """
    Test suite for service creation form validation.
    Ensures proper validation of service listing details.
    """

    def test_service_form_invalid_hourly_rate(self):
        """
        Test that the service form rejects invalid hourly rates.
        Verifies negative hourly rates are not allowed.
        """
        # Source Link: https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model
        form_data = {
            "title": "Test Service",
            "description": "Test Description",
            "category": "education",
            "hourly_rate": -50.00,  # Invalid negative rate
        }
        form = ServiceForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn(
            "hourly_rate", form.errors
        )  # Confirms error is related to hourly rate


class AvailabilityFormTests(TestCase):
    """
    Test suite for service availability form validation.
    Verifies proper handling of scheduling and time slot creation.
    """

    def test_availability_form_invalid_dates(self):
        """
        Test that the availability form rejects invalid dates.
        Ensures past dates cannot be used for scheduling.
        """
        # Source Link: https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.utils.timezone_override
        yesterday = timezone.now().date() - timedelta(days=1)
        form_data = {
            "date": yesterday,
            "start_time": "10:00",
            "end_time": "11:00",
            "location": "Test Location",
        }
        form = AvailabilityForm(data=form_data)
        self.assertFalse(form.is_valid())
        # Verifies specific error message for past dates
        self.assertIn(
            "Cannot create availability for past dates", form.errors["__all__"]
        )
