from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import UserProfile, Service, Availability, Appointment

class AuthenticationViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('sign_up')
        self.login_url = reverse('login')
        self.test_user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_signup_view_get(self):
        # Test GET request to signup page
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'skillflow/sign_up.html')

    def test_signup_view_post(self):
        # Test POST request to signup page
        response = self.client.post(self.signup_url, {
            'username': 'newuser',
            'password1': 'TestPass123!',
            'password2': 'TestPass123!'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful signup
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_view(self):
        # Test login functionality
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful login

class ServiceViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        # Create UserProfile for the test user
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            first_name='Test',
            last_name='User',
            email='test@example.com'
        )
        # Create test service
        self.service = Service.objects.create(
            title='Test Service',
            description='Test Description',
            category='education',
            hourly_rate=50.00,
            provider=self.user
        )
        self.create_service_url = reverse('service')
        self.service_detail_url = reverse('service_detail', args=[self.service.id])

class AppointmentViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create provider user
        self.provider = User.objects.create_user(
            username='provider',
            password='testpass123'
        )
        # Create client user
        self.client_user = User.objects.create_user(
            username='client',
            password='testpass123'
        )
        # Create service
        self.service = Service.objects.create(
            title='Test Service',
            description='Test Description',
            category='education',
            hourly_rate=50.00,
            provider=self.provider
        )