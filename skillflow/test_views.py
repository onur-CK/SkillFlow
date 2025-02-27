from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import UserProfile, Service, Availability, Appointment
from django.contrib.messages import get_messages


class AuthenticationViewTests(TestCase):
    # Test suite for authentication-related views including signup and login functionality.

    def setUp(self):
        """
        Initialize test environment with client and test user.
        Creates URLs for signup and login pages and a test user for authentication tests.
        Source link: https://stackoverflow.com/questions/57337720/writing-django-signup-form-tests-for-checking-new-user-creation
        """
        self.client = Client()
        self.signup_url = reverse("sign_up")
        self.login_url = reverse("login")
        self.test_user = User.objects.create_user(
            username="testuser", password="testpass123"
        )

    def test_signup_view_get(self):
        """
        Test GET request to signup page.
        Verifies that the signup page loads correctly and uses the correct template.
        Source Link: https://stackoverflow.com/questions/43501561/how-to-test-views-that-use-post-request-in-django
        """
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skillflow/sign_up.html")

    def test_signup_view_post(self):
        """
        Test POST request for user registration.
        Verifies that new users can be created successfully and are redirected properly.
        Source Links: https://stackoverflow.com/questions/43501561/how-to-test-views-that-use-post-request-in-django
        https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.post
        """
        # Shows how to test form submissions and check redirects
        response = self.client.post(
            self.signup_url,
            {
                "username": "newuser",
                "password1": "TestPass123!",
                "password2": "TestPass123!",
            },
        )
        self.assertEqual(
            response.status_code, 302
        )  # Should redirect after successful signup
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_login_view(self):
        """
        Test user login functionality.
        Verifies that users can log in successfully and are redirected appropriately.
        """
        response = self.client.post(
            self.login_url, {"username": "testuser", "password": "testpass123"}
        )
        self.assertEqual(
            response.status_code, 302
        )  # Should redirect after successful login


class ServiceViewTests(TestCase):
    # Test suite for service-related views including creation and management.

    def setUp(self):
        """
        Initialize test environment for service-related tests.
        Creates a test user, user profile, and service instance.
        Source Link: https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase
        """
        self.client = Client()
        # Create test user
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        # Create UserProfile for the test user
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            first_name="Test",
            last_name="User",
            email="test@example.com",
        )
        # Create test service
        self.service = Service.objects.create(
            title="Test Service",
            description="Test Description",
            category="education",
            hourly_rate=50.00,
            provider=self.user,
        )
        self.create_service_url = reverse("service")
        self.service_detail_url = reverse("service_detail", args=[self.service.id])


class AppointmentViewTests(TestCase):
    # Test suite for appointment-related functionality.

    def setUp(self):
        """
        Initialize test environment for appointment tests.
        Creates provider and client users, and a test service.
        """
        self.client = Client()
        # Create provider user
        self.provider = User.objects.create_user(
            username="provider", password="testpass123"
        )
        # Create client user
        self.client_user = User.objects.create_user(
            username="client", password="testpass123"
        )
        # Create service
        self.service = Service.objects.create(
            title="Test Service",
            description="Test Description",
            category="education",
            hourly_rate=50.00,
            provider=self.provider,
        )


class ViewsTestCase(TestCase):
    # Comprehensive test suite for various view functionalities.

    def setUp(self):
        """
        Initialize test environment with users, profiles, service, and availability.
        Creates test data necessary for various view tests.
        """
        # Create test users
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.provider = User.objects.create_user(username="provider", password="12345")

        # Create profiles for test users
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.provider_profile = UserProfile.objects.create(user=self.provider)

        # Create a test service
        self.service = Service.objects.create(
            title="Test Service",
            description="Test Description",
            category="education",
            hourly_rate=50.00,
            provider=self.provider,
        )

        # Create test availability
        self.tomorrow = timezone.now().date() + timedelta(days=1)
        self.availability = Availability.objects.create(
            provider=self.provider,
            service=self.service,
            date=self.tomorrow,
            start_time="10:00",
            end_time="11:00",
            location="Test Location",
        )

    def test_home_view(self):
        """
        Test home page view functionality.
        Verifies correct template rendering for both authenticated and unauthenticated users.
        Source Link: https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertTemplateUsed
        """
        # Test unauthenticated user access
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skillflow/about_us.html")

        # Test authenticated user access and redirection
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("home"))
        self.assertRedirects(response, reverse("index"))

    def test_edit_profile_view(self):
        """
        Test profile editing functionality.
        Verifies that users can view and update their profile information.
        """
        self.client.login(username="testuser", password="12345")

        # Test GET request to edit profile page
        response = self.client.get(reverse("edit_profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skillflow/edit_profile.html")

        # Test POST request with valid profile data
        # https://docs.djangoproject.com/en/5.0/topics/testing/tools/#testing-forms
        data = {
            "first_name": "Test",
            "last_name": "User",
            "email": "test@example.com",
            "bio": "Test bio",
        }
        response = self.client.post(reverse("edit_profile"), data)
        self.assertEqual(response.status_code, 302)

        # Verify profile was updated successfully
        updated_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(updated_profile.first_name, "Test")

    def test_manage_schedule_view(self):
        """
        Test functionality of the schedule management view.
        This test verifies that:
        1. Providers can access their schedule management page
        2. New availability slots can be created successfully
        3. The view handles GET and POST requests appropriately
        4. Created availability slots are associated with correct provider and service
        """
        # Log in as the service provider
        self.client.login(username="provider", password="12345")

        # Test GET request - should return schedule management page
        response = self.client.get(reverse("manage_schedule", args=[self.service.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skillflow/manage_schedule.html")

        # Test POST request to create new availability slot
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

        # Verify the availability slot was created with correct attributes
        self.assertTrue(
            Availability.objects.filter(
                provider=self.provider, service=self.service, location="Test Location"
            ).exists()
        )

    def test_book_appointment_view(self):
        """
        Test the appointment booking functionality.
        This test ensures:
        1. Clients can access the booking page
        2. Appointments can be created successfully
        3. The view handles both GET and POST requests correctly
        4. Created appointments are properly associated with client and availability
        """
        # Log in as a client user
        self.client.login(username="testuser", password="12345")

        # Test GET request - should show booking page
        response = self.client.get(reverse("book_appointment", args=[self.service.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skillflow/book_appointment.html")

        # Test POST request to create new appointment
        data = {"availability": self.availability.id}
        response = self.client.post(
            reverse("book_appointment", args=[self.service.id]), data
        )
        self.assertEqual(response.status_code, 302)

        # Verify appointment was created with correct associations
        self.assertTrue(
            Appointment.objects.filter(
                availability=self.availability, client=self.user
            ).exists()
        )

    def test_update_appointment_status(self):
        """
        Test appointment status update functionality.

        Verifies:
        1. Providers can update appointment statuses
        2. Status changes are correctly saved
        3. Proper redirection occurs after status update
        """
        # Log in as service provider
        self.client.login(username="provider", password="12345")

        # Create a test appointment
        appointment = Appointment.objects.create(
            availability=self.availability, client=self.user, status="pending"
        )

        # Test status update to 'confirmed'
        data = {"status": "confirmed"}
        response = self.client.post(
            reverse("update_appointment_status", args=[appointment.id]), data
        )
        self.assertEqual(response.status_code, 302)

        # Verify status was updated correctly
        updated_appointment = Appointment.objects.get(id=appointment.id)
        self.assertEqual(updated_appointment.status, "confirmed")

    def test_service_detail_view(self):
        """
        Test service detail view functionality.
        Ensures:
        1. Service details are correctly displayed
        2. Correct template is used
        3. Service context is properly passed to template
        """
        response = self.client.get(reverse("service_detail", args=[self.service.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skillflow/service_detail.html")
        self.assertEqual(response.context["service"], self.service)

    def test_category_services_view(self):
        """
        Test category-based service filtering.
        Verifies:
        1. Services can be filtered by category
        2. Correct template is used
        3. Filtered services are passed to template context
        """
        response = self.client.get(reverse("category_services", args=["education"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skillflow/index.html")
        self.assertEqual(list(response.context["services"]), [self.service])

    def test_delete_account(self):
        """
        Test account deletion functionality.
        Ensures:
        1. Users can delete their accounts
        2. Proper redirection occurs after deletion
        3. User data is actually removed from database
        """
        self.client.login(username="testuser", password="12345")
        response = self.client.post(reverse("delete_account"))
        self.assertRedirects(response, reverse("about_us"))
        self.assertFalse(User.objects.filter(username="testuser").exists())

    def test_delete_service(self):
        """
        Test service deletion functionality.
        Verifies:
        1. Providers can delete their services
        2. Proper redirection occurs after deletion
        3. Service is actually removed from database
        """
        # Source Link: https://docs.djangoproject.com/en/5.0/topics/testing/tools/#assertredirects
        self.client.login(username="provider", password="12345")
        response = self.client.post(reverse("delete_service", args=[self.service.id]))
        self.assertRedirects(response, reverse("my_services"))
        self.assertFalse(Service.objects.filter(id=self.service.id).exists())

    def test_delete_availability(self):
        """
        Test availability slot deletion functionality.
        Ensures:
        1. Providers can delete availability slots
        2. Proper redirection occurs after deletion
        3. Availability slot is removed from database
        """
        self.client.login(username="provider", password="12345")
        response = self.client.post(
            reverse("delete_availability", args=[self.service.id, self.availability.id])
        )
        self.assertRedirects(
            response, reverse("manage_schedule", args=[self.service.id])
        )
        self.assertFalse(Availability.objects.filter(id=self.availability.id).exists())


class AdditionalViewTests(TestCase):
    def setUp(self):
        # Create test client
        self.client = Client()

        # Create test users
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.provider = User.objects.create_user(username="provider", password="12345")

        # Create profiles
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.provider_profile = UserProfile.objects.create(user=self.provider)

        # Create service
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

    def test_login_view_invalid_credentials(self):
        # Test login view with invalid credentials
        # Source Link: https://docs.djangoproject.com/en/5.0/ref/contrib/messages/#testing-messages
        response = self.client.post(
            reverse("login"), {"username": "testuser", "password": "wrongpassword"}
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertIn("Invalid username or password.", [m.message for m in messages])

    def test_service_creation_invalid_data(self):
        # Test service creation with invalid data
        self.client.login(username="testuser", password="12345")
        response = self.client.post(
            reverse("service"),
            {
                "title": "",  # Invalid: empty title
                "description": "Test",
                "category": "education",
                "hourly_rate": 50,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Service.objects.filter(description="Test").exists())

    def test_book_appointment_own_service(self):
        # Test attempting to book own service
        self.client.login(username="provider", password="12345")
        response = self.client.post(
            reverse("book_appointment", args=[self.service.id]),
            {"availability": self.availability.id},
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertIn(
            "You cannot book your own service.", [m.message for m in messages]
        )

    def test_book_appointment_already_booked(self):
        # Test booking an already booked slot

        # First booking
        self.client.login(username="testuser", password="12345")
        self.client.post(
            reverse("book_appointment", args=[self.service.id]),
            {"availability": self.availability.id},
        )

        # Create another user and attempt to book same slot
        user2 = User.objects.create_user(username="testuser2", password="12345")
        self.client.login(username="testuser2", password="12345")
        response = self.client.post(
            reverse("book_appointment", args=[self.service.id]),
            {"availability": self.availability.id},
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertIn(
            "Sorry, this time slot has already been booked.",
            [m.message for m in messages],
        )

    def test_manage_schedule_overlapping_slots(self):
        # Test creating overlapping availability slots
        self.client.login(username="provider", password="12345")

        # Create first slot
        self.client.post(
            reverse("manage_schedule", args=[self.service.id]),
            {
                "date": self.tomorrow,
                "start_time": "14:00",
                "end_time": "15:00",
                "location": "Test Location",
            },
        )

        # Try to create overlapping slot
        response = self.client.post(
            reverse("manage_schedule", args=[self.service.id]),
            {
                "date": self.tomorrow,
                "start_time": "14:30",
                "end_time": "15:30",
                "location": "Test Location",
            },
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertIn(
            "This time slot overlaps with an existing schedule.",
            [m.message for m in messages],
        )

    def test_cancel_booked_availability(self):
        # Test attempting to delete a booked availability slot
        # Book the slot first
        self.client.login(username="testuser", password="12345")
        self.client.post(
            reverse("book_appointment", args=[self.service.id]),
            {"availability": self.availability.id},
        )

        # Try to delete the booked slot
        self.client.login(username="provider", password="12345")
        response = self.client.post(
            reverse("delete_availability", args=[self.service.id, self.availability.id])
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertIn(
            "Cannot delete a booked time slot.", [m.message for m in messages]
        )

    def test_cancel_appointment_last_minute(self):
        # Test cancelling appointment within 24 hours

        self.client.login(username="testuser", password="12345")

        # Create availability for today
        today = timezone.now()
        availability = Availability.objects.create(
            provider=self.provider,
            service=self.service,
            # Source Link: https://docs.djangoproject.com/en/5.0/topics/testing/tools/#time-zones
            date=today.date(),
            start_time=(today + timedelta(hours=2)).time(),  # 2 hours from now
            end_time=(today + timedelta(hours=3)).time(),  # 3 hours from now
            location="Test Location",
        )

        # Create and confirm appointment
        appointment = Appointment.objects.create(
            availability=availability, client=self.user, status="confirmed"
        )

        # Try to cancel the appointment
        response = self.client.post(
            reverse("update_appointment_status", args=[appointment.id]),
            {"status": "cancelled"},
        )

        # Verify the error message
        messages = list(get_messages(response.wsgi_request))
        self.assertIn(
            "Appointments must be cancelled at least 24 hours in advance as per our cancellation policy.",
            [m.message for m in messages],
        )

        # Verify appointment wasn't cancelled
        appointment.refresh_from_db()
        self.assertEqual(appointment.status, "confirmed")

    def test_edit_service_unauthorized(self):
        # Test editing service without authorization
        # Source Link: https://docs.djangoproject.com/en/5.0/topics/auth/default/#authentication-in-web-requests
        self.client.login(
            username="testuser", password="12345"
        )  # Not the service provider
        response = self.client.get(reverse("edit_service", args=[self.service.id]))
        self.assertEqual(response.status_code, 403)  # Should return Forbidden

    def test_edit_profile_form_validation(self):
        # Test profile editing with invalid data
        self.client.login(username="testuser", password="12345")
        response = self.client.post(
            reverse("edit_profile"),
            {"email": "invalid-email", "bio": "Test bio"},  # Invalid email format
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertIn(
            "Please check all required fields and try again.",
            [m.message for m in messages],
        )

    def test_manage_schedule_invalid_times(self):
        # Test creating availability with invalid time range
        self.client.login(username="provider", password="12345")
        response = self.client.post(
            reverse("manage_schedule", args=[self.service.id]),
            {
                "date": self.tomorrow,
                "start_time": "15:00",
                "end_time": "14:00",  # End time before start time
                "location": "Test Location",
            },
        )
        self.assertFalse(
            Availability.objects.filter(
                provider=self.provider, start_time="15:00", end_time="14:00"
            ).exists()
        )
