from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .models import UserProfile, Service, Availability, Appointment
from django.core.exceptions import ValidationError

class UserProfileTests(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            first_name='Test',
            last_name='User',
            email='test@example.com',
            bio='Test bio'
        )

    def test_profile_creation(self):
        # Test that profile is created correctly
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.first_name, 'Test')
        self.assertEqual(self.profile.last_name, 'User')
        self.assertEqual(self.profile.email, 'test@example.com')
        self.assertEqual(self.profile.bio, 'Test bio')

    def test_profile_str_method(self):
        # Test the string representation of UserProfile
        self.assertEqual(str(self.profile), 'testuser')

class ServiceTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='provider',
            password='testpass123'
        )
        self.service = Service.objects.create(
            title='Test Service',
            description='Test Description',
            category='education',
            hourly_rate=50.00,
            provider=self.user
        )

    def test_service_creation(self):
        # Test that service is created correctly
        self.assertEqual(self.service.title, 'Test Service')
        self.assertEqual(self.service.category, 'education')
        self.assertEqual(float(self.service.hourly_rate), 50.00)
        self.assertEqual(self.service.provider, self.user)

    def test_service_str_method(self):
        # Test the string representation of Service
        self.assertEqual(str(self.service), 'Test Service')

class AvailabilityTests(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='provider',
            password='testpass123'
        )
        # Create test service
        self.service = Service.objects.create(
            title='Test Service',
            description='Test Description',
            category='education',
            hourly_rate=50.00,
            provider=self.user
        )
        # Create test availability
        self.tomorrow = timezone.now().date() + timedelta(days=1)
        self.availability = Availability.objects.create(
            provider=self.user,
            service=self.service,
            date=self.tomorrow,
            start_time='10:00',
            end_time='11:00',
            location='Test Location'
        )

    def test_availability_creation(self):
        # Test that availability is created correctly
        self.assertEqual(self.availability.provider, self.user)
        self.assertEqual(self.availability.service, self.service)
        self.assertEqual(self.availability.location, 'Test Location')
        self.assertFalse(self.availability.is_booked)

    def test_invalid_dates(self):
        # Test that past dates are not allowed
        yesterday = timezone.now().date() - timedelta(days=1)
        with self.assertRaises(ValidationError):
            availability = Availability.objects.create(
                provider=self.user,
                service=self.service,
                date=yesterday,
                start_time='10:00',
                end_time='11:00',
                location='Test Location'
            )
            availability.full_clean()  # This triggers the validation

class AppointmentTests(TestCase):
    def setUp(self):
        # Create provider and client users
        self.provider = User.objects.create_user(
            username='provider',
            password='testpass123'
        )
        self.client_user = User.objects.create_user(
            username='client',
            password='testpass123'
        )
        
        # Create service and availability
        self.service = Service.objects.create(
            title='Test Service',
            description='Test Description',
            category='education',
            hourly_rate=50.00,
            provider=self.provider
        )
        self.tomorrow = timezone.now().date() + timedelta(days=1)
        self.availability = Availability.objects.create(
            provider=self.provider,
            service=self.service,
            date=self.tomorrow,
            start_time='10:00',
            end_time='11:00',
            location='Test Location'
        )

    def test_appointment_creation(self):
        # Test that appointment is created correctly
        appointment = Appointment.objects.create(
            availability=self.availability,
            client=self.client_user,
            status='pending'
        )
        self.assertEqual(appointment.client, self.client_user)
        self.assertEqual(appointment.status, 'pending')
        self.assertEqual(appointment.availability, self.availability)

    def test_appointment_status_changes(self):
        # Test appointment status transitions
        appointment = Appointment.objects.create(
            availability=self.availability,
            client=self.client_user,
            status='pending'
        )
        
        # Test confirming appointment
        appointment.status = 'confirmed'
        appointment.save()
        self.assertEqual(appointment.status, 'confirmed')
        
        # Test cancelling appointment
        appointment.status = 'cancelled'
        appointment.save()
        self.assertEqual(appointment.status, 'cancelled')