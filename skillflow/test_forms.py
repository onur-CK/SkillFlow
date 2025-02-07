from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .forms import SignUpForm, UserProfileForm, ServiceForm, AvailabilityForm

class SignUpFormTests(TestCase):
    def test_signup_form_valid_data(self):
        # Test form with valid data
        form_data = {
            'username': 'testuser',
            'password1': 'TestPass123!',
            'password2': 'TestPass123!'
        }
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_signup_form_invalid_data(self):
        # Test form with invalid data
        # Test with mismatched passwords
        form_data = {
            'username': 'testuser',
            'password1': 'TestPass123!',
            'password2': 'DifferentPass123!'
        }
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

class UserProfileFormTests(TestCase):
    def test_profile_form_valid_data(self):
        # Test form with valid data
        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'bio': 'Test bio'
        }
        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_profile_form_bio_length(self):
        # Test bio length validation
        # Create bio text that exceeds max length
        long_bio = 'x' * 201  # Bio max length is 200
        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'bio': long_bio
        }
        form = UserProfileForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('bio', form.errors)

class ServiceFormTests(TestCase):
    def test_service_form_valid_data(self):
        # Test form with valid data
        form_data = {
            'title': 'Test Service',
            'description': 'Test Description',
            'category': 'education',
            'hourly_rate': 50.00
        }
        form = ServiceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_service_form_invalid_hourly_rate(self):
        # Test hourly rate validation
        # Test with negative hourly rate
        form_data = {
            'title': 'Test Service',
            'description': 'Test Description',
            'category': 'education',
            'hourly_rate': -50.00
        }
        form = ServiceForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('hourly_rate', form.errors)

class AvailabilityFormTests(TestCase):
    def test_availability_form_valid_data(self):
        # Test form with valid data
        tomorrow = timezone.now().date() + timedelta(days=1)
        form_data = {
            'date': tomorrow,
            'start_time': '10:00',
            'end_time': '11:00',
            'location': 'Test Location'
        }
        form = AvailabilityForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_availability_form_invalid_dates(self):
        # Test date validation
        # Test with past date
        yesterday = timezone.now().date() - timedelta(days=1)
        form_data = {
            'date': yesterday,
            'start_time': '10:00',
            'end_time': '11:00',
            'location': 'Test Location'
        }
        form = AvailabilityForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors)

    def test_availability_form_invalid_times(self):
        # Test time validation
        # Test with end time before start time
        tomorrow = timezone.now().date() + timedelta(days=1)
        form_data = {
            'date': tomorrow,
            'start_time': '11:00',
            'end_time': '10:00',
            'location': 'Test Location'
        }
        form = AvailabilityForm(data=form_data)
        self.assertFalse(form.is_valid())