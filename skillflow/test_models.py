from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .models import UserProfile, Service, Availability, Appointment
from django.core.exceptions import ValidationError
from django.urls import reverse


class UserProfileTests(TestCase):
    # Source Links: https://docs.djangoproject.com/en/5.0/topics/testing/overview/#testcase
    # https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            first_name="Test",
            last_name="User",
            email="test@example.com",
            bio="Test bio",
        )

    def test_profile_creation(self):
        # Test that profile is created correctly
        # Source Link: https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase.assertEqual
        self.assertEqual(self.profile.user.username, "testuser")
        self.assertEqual(self.profile.first_name, "Test")
        self.assertEqual(self.profile.last_name, "User")
        self.assertEqual(self.profile.email, "test@example.com")
        self.assertEqual(self.profile.bio, "Test bio")

    def test_profile_str_method(self):
        # Test the string representation of UserProfile
        self.assertEqual(str(self.profile), "testuser")


class ServiceTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="provider", password="testpass123"
        )
        self.service = Service.objects.create(
            title="Test Service",
            description="Test Description",
            category="education",
            hourly_rate=50.00,
            provider=self.user,
        )

    def test_service_creation(self):
        # Test that service is created correctly
        self.assertEqual(self.service.title, "Test Service")
        self.assertEqual(self.service.category, "education")
        self.assertEqual(float(self.service.hourly_rate), 50.00)
        self.assertEqual(self.service.provider, self.user)

    def test_service_str_method(self):
        # Test the string representation of Service
        self.assertEqual(str(self.service), "Test Service")


class AvailabilityTests(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username="provider", password="testpass123"
        )
        # Create test service
        self.service = Service.objects.create(
            title="Test Service",
            description="Test Description",
            category="education",
            hourly_rate=50.00,
            provider=self.user,
        )
        # Create test availability
        self.tomorrow = timezone.now().date() + timedelta(days=1)
        self.availability = Availability.objects.create(
            provider=self.user,
            service=self.service,
            date=self.tomorrow,
            start_time="10:00",
            end_time="11:00",
            location="Test Location",
        )

    def test_availability_creation(self):
        # Test that availability is created correctly
        self.assertEqual(self.availability.provider, self.user)
        self.assertEqual(self.availability.service, self.service)
        self.assertEqual(self.availability.location, "Test Location")
        self.assertFalse(self.availability.is_booked)

    # Source Link: https://docs.djangoproject.com/en/5.0/ref/validators/#modelvalidator-classes
    # https://stackoverflow.com/questions/21458387/how-to-test-validation-errors-with-django-model-tests
    def test_invalid_dates(self):
        # Test that past dates are not allowed
        yesterday = timezone.now().date() - timedelta(days=1)
        with self.assertRaises(ValidationError):
            availability = Availability.objects.create(
                provider=self.user,
                service=self.service,
                date=yesterday,
                start_time="10:00",
                end_time="11:00",
                location="Test Location",
            )
            availability.full_clean()  # This triggers the validation


class AppointmentTests(TestCase):
    def setUp(self):
        # Create provider and client users
        self.provider = User.objects.create_user(
            username="provider", password="testpass123"
        )
        self.client_user = User.objects.create_user(
            username="client", password="testpass123"
        )

        # Create service and availability
        self.service = Service.objects.create(
            title="Test Service",
            description="Test Description",
            category="education",
            hourly_rate=50.00,
            provider=self.provider,
        )
        self.tomorrow = timezone.now().date() + timedelta(days=1)
        self.availability = Availability.objects.create(
            provider=self.provider,
            service=self.service,
            date=self.tomorrow,
            start_time="10:00",
            end_time="11:00",
            location="Test Location",
        )

    def test_appointment_creation(self):
        # Test that appointment is created correctly
        appointment = Appointment.objects.create(
            availability=self.availability, client=self.client_user, status="pending"
        )
        self.assertEqual(appointment.client, self.client_user)
        self.assertEqual(appointment.status, "pending")
        self.assertEqual(appointment.availability, self.availability)

    # Source Link: https://docs.djangoproject.com/en/5.0/topics/testing/tools/#testing-database-state
    def test_appointment_status_changes(self):
        # Test appointment status transitions
        appointment = Appointment.objects.create(
            availability=self.availability, client=self.client_user, status="pending"
        )

        # Test confirming appointment
        appointment.status = "confirmed"
        appointment.save()
        self.assertEqual(appointment.status, "confirmed")

        # Test cancelling appointment
        appointment.status = "cancelled"
        appointment.save()
        self.assertEqual(appointment.status, "cancelled")


class ViewsTestCase(TestCase):
    # Source Links: https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client
    # https://stackoverflow.com/questions/2619102/djangos-self-client-login-does-not-work-in-unit-tests
    def setUp(self):
        # Create test users
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.provider = User.objects.create_user(username="provider", password="12345")

        # Create profiles
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.provider_profile = UserProfile.objects.create(user=self.provider)

        # Create a service
        self.service = Service.objects.create(
            title="Test Service",
            description="Test Description",
            category="education",
            hourly_rate=50.00,
            provider=self.provider,
        )

        # Create availability
        self.tomorrow = timezone.now().date() + timedelta(days=1)
        self.availability = Availability.objects.create(
            provider=self.provider,
            service=self.service,
            date=self.tomorrow,
            start_time="10:00",
            end_time="11:00",
            location="Test Location",
        )

    # Source Link: https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.get
    # https://stackoverflow.com/questions/16143149/django-testing-check-messages-for-a-view
    def test_home_view(self):
        # Test unauthenticated user
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skillflow/about_us.html")

        # Test authenticated user
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("home"))
        self.assertRedirects(response, reverse("index"))

    # Source Link: https://stackoverflow.com/questions/7304248/how-should-i-write-tests-for-forms-in-django
    def test_edit_profile_view(self):
        self.client.login(username="testuser", password="12345")

        # Test GET request
        response = self.client.get(reverse("edit_profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skillflow/edit_profile.html")

        # Test POST request with valid data
        data = {
            "first_name": "Test",
            "last_name": "User",
            "email": "test@example.com",
            "bio": "Test bio",
        }
        response = self.client.post(reverse("edit_profile"), data)
        self.assertEqual(response.status_code, 302)

        # Verify profile was updated
        updated_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(updated_profile.first_name, "Test")

    def test_manage_schedule_view(self):
        self.client.login(username="provider", password="12345")

        # Test GET request
        response = self.client.get(reverse("manage_schedule", args=[self.service.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skillflow/manage_schedule.html")

        # Test POST request with valid data
        data = {
            "date": (timezone.now().date() + timedelta(days=2)).strftime("%Y-%m-%d"),
            "start_time": "14:00",
            "end_time": "15:00",
            "location": "Test Location",
        }
        response = self.client.post(
            reverse("manage_schedule", args=[self.service.id]), data
        )
        self.assertEqual(response.status_code, 302)

        # Verify new availability was created
        self.assertTrue(
            Availability.objects.filter(
                provider=self.provider, service=self.service, location="Test Location"
            ).exists()
        )

    def test_book_appointment_view(self):
        self.client.login(username="testuser", password="12345")

        # Test GET request
        response = self.client.get(reverse("book_appointment", args=[self.service.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skillflow/book_appointment.html")

        # Test POST request with valid data
        data = {"availability": self.availability.id}
        response = self.client.post(
            reverse("book_appointment", args=[self.service.id]), data
        )
        self.assertEqual(response.status_code, 302)

        # Verify appointment was created
        self.assertTrue(
            Appointment.objects.filter(
                availability=self.availability, client=self.user
            ).exists()
        )

    def test_update_appointment_status(self):
        self.client.login(username="provider", password="12345")

        # Create an appointment
        appointment = Appointment.objects.create(
            availability=self.availability, client=self.user, status="pending"
        )

        # Test confirming appointment
        data = {"status": "confirmed"}
        response = self.client.post(
            reverse("update_appointment_status", args=[appointment.id]), data
        )
        self.assertEqual(response.status_code, 302)

        # Verify status was updated
        updated_appointment = Appointment.objects.get(id=appointment.id)
        self.assertEqual(updated_appointment.status, "confirmed")

    def test_service_detail_view(self):
        """
        Test service detail view functionality.
        Verifies that:
        1. Service detail page loads successfully (200 status code)
        2. Correct template is used for rendering
        3. Service object in context matches the requested service
        """
        response = self.client.get(reverse("service_detail", args=[self.service.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skillflow/service_detail.html")
        self.assertEqual(response.context["service"], self.service)

    def test_category_services_view(self):
        """
        Test category filtering functionality.
        Verifies that:
        1. Category filter page loads successfully
        2. Correct template is used for displaying filtered services
        3. Only services from requested category are displayed
        4. Services are properly passed to the template context
        """
        response = self.client.get(reverse("category_services", args=["education"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skillflow/index.html")
        self.assertEqual(list(response.context["services"]), [self.service])

    def test_delete_account(self):
        """
        Test account deletion functionality.
        Verifies that:
        1. User can successfully log in before deletion
        2. Account deletion request is processed correctly
        3. User is redirected to about page after deletion
        4. User account is actually removed from the database
        """
        self.client.login(username="testuser", password="12345")
        response = self.client.post(reverse("delete_account"))
        self.assertRedirects(response, reverse("about_us"))
        self.assertFalse(User.objects.filter(username="testuser").exists())

    def test_delete_service(self):
        """
        Test service deletion functionality.
        Verifies that:
        1. Service provider can log in
        2. Service deletion request is processed correctly
        3. Provider is redirected to their services page
        4. Service is actually removed from the database
        """
        self.client.login(username="provider", password="12345")
        response = self.client.post(reverse("delete_service", args=[self.service.id]))
        self.assertRedirects(response, reverse("my_services"))
        self.assertFalse(Service.objects.filter(id=self.service.id).exists())

    def test_delete_availability(self):
        """
        Test availability slot deletion functionality.
        Verifies that:
        1. Provider can log in to manage their schedule
        2. Availability deletion request is processed
        3. Provider is redirected to schedule management page
        4. Availability slot is actually removed from the database
        """
        self.client.login(username="provider", password="12345")
        response = self.client.post(
            reverse("delete_availability", args=[self.service.id, self.availability.id])
        )
        self.assertRedirects(
            response, reverse("manage_schedule", args=[self.service.id])
        )
        self.assertFalse(Availability.objects.filter(id=self.availability.id).exists())
