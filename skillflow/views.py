# views.py - Main application views for SkillFlow
# Contains view functions for handling HTTP requests and responses
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserProfileForm, ServiceForm, AvailabilityForm
from .models import UserProfile, Service, Availability, Appointment
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
import logging
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.db import transaction, models
from django.db import IntegrityError
from datetime import datetime
from django.http import JsonResponse
from django.conf import settings
from django.templatetags.static import static
from django.http import JsonResponse


def check_static_settings(request):

    # Debug view to check static files configuration

    config = {
        "STATIC_URL": settings.STATIC_URL,
        "STATIC_ROOT": settings.STATIC_ROOT,
        "STATICFILES_DIRS": settings.STATICFILES_DIRS,
        "DEBUG": settings.DEBUG,
        "STATICFILES_STORAGE": settings.STATICFILES_STORAGE,
    }
    return JsonResponse(config)


def check_ssl_settings(request):
    """
    Diagnostic view to check SSL configuration settings.
    Returns JSON response with current SSL-related settings.
    """
    ssl_settings = {
        "SECURE_SSL_REDIRECT": getattr(settings, "SECURE_SSL_REDIRECT", False),
        "SECURE_HSTS_SECONDS": getattr(settings, "SECURE_HSTS_SECONDS", 0),
        "SECURE_HSTS_INCLUDE_SUBDOMAINS": getattr(
            settings, "SECURE_HSTS_INCLUDE_SUBDOMAINS", False
        ),
        "SECURE_HSTS_PRELOAD": getattr(settings, "SECURE_HSTS_PRELOAD", False),
        "SESSION_COOKIE_SECURE": getattr(
            settings, "SESSION_COOKIE_SECURE", False
        ),
        "CSRF_COOKIE_SECURE": getattr(settings, "CSRF_COOKIE_SECURE", False),
        "SECURE_BROWSER_XSS_FILTER": getattr(
            settings, "SECURE_BROWSER_XSS_FILTER", False
        ),
        "is_secure": request.is_secure(),
        "protocol": request.META.get("HTTP_X_FORWARDED_PROTO", ""),
    }
    return JsonResponse(ssl_settings)


# Configure logging for the views module
logger = logging.getLogger(__name__)

# This module contains all view functions for the SkillFlow application.
# Views handle HTTP requests and return appropriate responses.


def about_us(request):
    """
    Renders the about page with platform information.
    Simple view that returns the about_us.html template.
    """
    return render(request, "skillflow/about_us.html")


def sign_up(request):
    """
    Handles user registration process.
    POST: Creates new user account and associated profile
    GET: Displays registration form
    Creates UserProfile for new users and logs them in automatically.
    Redirects to index page on successful registration.
    """
    if request.method == "POST":
        form = SignUpForm(request.POST)
        # https://stackoverflow.com/questions/69280755/valueerror-at-the-view-leads-views-home-page-didnt-return-an-httpresponse-obj/69280887
        if form.is_valid():
            user = form.save()
            # Create UserProfile for the new user
            UserProfile.objects.create(user=user)
            auth_login(request, user)
            # https://docs.djangoproject.com/en/5.1/ref/contrib/messages/
            messages.success(
                request,
                f"Welcome, {user.username}! It`s great to have you here."
            )
            return redirect("index")
    else:
        form = SignUpForm()
    return render(request, "skillflow/sign_up.html", {"form": form})


def login(request):
    """
    Handles user authentication.
    POST: Authenticates user credentials and creates session
    GET: Displays login form
    Provides different welcome messages for first-time vs returning users.
    Redirects to index page on successful login.
    """
    # https://docs.djangoproject.com/en/5.1/topics/auth/default/#auth-web-requests
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            first_login = (
                user.last_login is None
            )  # Check if the user has logged in before
            auth_login(request, user)
            if first_login:
                # https://docs.djangoproject.com/en/5.1/ref/contrib/messages/
                messages.success(
                    request,
                    f"Welcome, {username}! It’s great to have you here."
                )
            else:
                messages.success(request, f"Welcome back, {username}!")
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")
    return render(request, "skillflow/login.html")


@login_required
def index(request):
    """
    Main dashboard view showing service listings.
    Requires authentication.
    Displays services filtered by category if category parameter is provided.
    Orders services by creation date.
    """
    category = request.GET.get("category")
    if category:
        services = Service.objects.filter(
            category=category
        ).order_by("created_at")
    else:
        services = Service.objects.all().order_by("created_at")
    return render(
        request,
        "skillflow/index.html",
        {"services": services, "active_category": category},
    )


@login_required
def service(request):
    """
    Handles creation of new service listings.
    POST: Creates new service with current user as provider
    GET: Displays service creation form
    Requires authentication. Associates service with current user.
    Redirects to index on successful creation.
    """
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.provider = request.user
            service.save()
            # https://docs.djangoproject.com/en/5.1/ref/contrib/messages/
            messages.success(
                request,
                f'Your service "{service.title}" '
                'has been updated successfully.'
            )
            return redirect("index")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ServiceForm()
    return render(request, "skillflow/service.html", {"form": form})


@login_required
def edit_profile(request):
    """
    Handles user profile editing.
    POST: Updates user profile information
    GET: Displays profile editing form
    Creates profile if it doesn't exist.
    Shows success/error messages for form submission.
    """
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        # https://docs.djangoproject.com/en/5.1/ref/forms/validation/
        if form.is_valid():
            form.save()
            # https://docs.djangoproject.com/en/5.1/ref/contrib/messages/
            messages.success(request, "Profile updated successfully!")
            return redirect("edit_profile")
        else:
            messages.error(
                request,
                "Please check all required fields and try again.")
    else:
        form = UserProfileForm(instance=profile)
    return render(
        request,
        "skillflow/edit_profile.html",
        {
            "form": form,
            "profile": profile
        }
    )


@login_required
def manage_account(request):
    """
    Displays account management page.
    Simple view that renders the account management template.
    Requires authentication.
    """
    return render(request, "skillflow/manage_account.html")


@login_required
def delete_account(request):
    """
    Handles account deletion.
    POST: Deletes user account and all associated data
    Requires authentication.
    Redirects to about page after deletion.
    """
    if request.method == "POST":
        user = request.user
        username = user.username
        user.delete()
        # Success message
        messages.success(
            request,
            f"Account for {username} has been successfully deleted."
            "We're sorry to see you go."
        )
        return redirect("about_us")
    return redirect("manage_account")


def logout_view(request):
    """
    Handles user logout.
    POST: Logs out user and ends session
    GET: Displays logout confirmation page
    Shows success message after logout.
    Redirects to about page.
    """
    if request.method == "POST":
        auth_logout(request)
        # https://docs.djangoproject.com/en/5.1/ref/contrib/messages/
        messages.success(request, "You have been logged out successfully.")
        return redirect("about_us")
    return render(request, "skillflow/logout.html")


def home(request):
    """
    Landing page view.
    Redirects authenticated users to index.
    Shows about page for non-authenticated users.
    """
    if request.user.is_authenticated:
        return redirect("index")
    return render(request, "skillflow/about_us.html")


@login_required
def service(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        # https://docs.djangoproject.com/en/5.1/ref/forms/validation/
        if form.is_valid():
            service = form.save(commit=False)
            service.provider = request.user
            service.save()
            # https://docs.djangoproject.com/en/5.1/ref/contrib/messages/
            messages.success(request, "Service listed successfully!")
            return redirect("index")
        else:
            messages.error(
                request,
                "Please check all required fields and try again."
            )
    else:
        form = ServiceForm()
    return render(request, "skillflow/service.html", {"form": form})


def category_services(request, category):
    """
    Displays services filtered by category.
    Takes category parameter to filter services.
    Orders services by creation date.
    """
    services = Service.objects.filter(category=category).order_by("created_at")
    return render(
        request,
        "skillflow/index.html",
        {"services": services, "active_category": category},
    )


@login_required
def edit_service(request, service_id):
    """
    Handles service editing.
    POST: Updates service information
    GET: Displays service editing form
    Requires authentication and verifies user owns service.
    Shows success/error messages for form submission.
    """
    # https://docs.djangoproject.com/en/5.1/topics/http/shortcuts/#get-object-or-404
    service = get_object_or_404(Service, id=service_id)

    # Check if the current user is the service provider
    if service.provider != request.user:
        raise PermissionDenied

    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, "Service updated successfully!")
            return redirect("my_services")
        else:
            messages.error(
                request,
                "Please check all required fields and try again."
            )
    else:
        form = ServiceForm(instance=service)

    return render(
        request,
        "skillflow/edit_service.html",
        {"form": form, "service": service}
    )


@login_required
def delete_service(request, service_id):
    """
    Handles service deletion.
    POST: Deletes service if user is owner
    Requires authentication and verifies user owns service.
    Shows success/error messages and redirects to my_services.
    """
    service = get_object_or_404(Service, id=service_id)
    if service.provider != request.user:
        messages.error(
            request,
            "You do not have permission to delete this service."
        )
        return redirect("my_services")

    if request.method == "POST":
        service.delete()
        messages.success(request, "Service deleted successfully.")
        return redirect("my_services")


@login_required
def my_services(request):
    """
    Displays user's service listings.
    Shows services where current user is provider.
    Orders services by creation date (newest first).
    """
    # Source Link of Django date query from newest to oldest:
    # https://stackoverflow.com/questions/30314741/django-date-query-from-newest-to-oldest
    user_services = Service.objects.filter(provider=request.user).order_by(
        "-created_at"
    )
    return render(
        request, "skillflow/my_services.html", {"user_services": user_services}
    )


@login_required
def book_appointment(request, service_id):
    """
    Handles appointment booking process.
    POST: Creates new appointment for selected time slot
    GET: Displays available time slots for booking

    Includes validation for:
    - Past dates
    - Already booked slots
    - Booking own service

    Uses transaction.atomic() for database consistency.
    Shows success/error messages and redirects appropriately.
    """
    service = get_object_or_404(Service, id=service_id)

    if request.method == "POST":
        availability_id = request.POST.get("availability")
        availability = get_object_or_404(Availability, id=availability_id)

        # Check if the date is a past date
        if availability.date < timezone.now().date():
            messages.error(request, "Please select a future date.")
            return redirect("book_appointment", service_id=service_id)

        # Check if the availability is already booked
        if availability.is_booked:
            messages.error(
                request,
                "Sorry, this time slot has already been booked."
            )
            return redirect("book_appointment", service_id=service_id)

        # Check if trying to book own service
        if service.provider == request.user:
            messages.error(request, "You cannot book your own service.")
            return redirect("book_appointment", service_id=service_id)

        try:
            # Use transaction.atomic() to ensure database consistency
            # https://www.geeksforgeeks.org/transaction-atomic-with-django/
            # https://docs.djangoproject.com/en/5.1/topics/db/transactions/
            with transaction.atomic():
                # Create appointment and mark availability as booked
                appointment = Appointment.objects.create(
                    availability=availability,
                    client=request.user,
                    status="pending"
                )
                availability.is_booked = True
                availability.save()

                # Store appointment success in session
                request.session["appointment_success"] = True
                request.session["appointment_service"] = service.title

            return redirect("appointments")

        except Exception as e:
            messages.error(
                request,
                "There was an error booking the appointment. Please try again."
            )
            return redirect("book_appointment", service_id=service_id)

    # Get available time slots
    availabilities = Availability.objects.filter(
        service=service, is_booked=False, date__gte=timezone.now().date()
    ).order_by("date", "start_time")

    return render(
        request,
        "skillflow/book_appointment.html",
        {"service": service, "availabilities": availabilities},
    )


@login_required
def view_appointments(request):
    """
    Displays user's appointments.
    Shows both:
    - Appointments for services user provides
    - Appointments user has booked as client

    Orders appointments by date and time.
    Handles appointment success messages from session.
    """
    if request.session.pop("appointment_success", False):
        service_title = request.session.pop("appointment_service", "")
        messages.success(
            request, f"Appointment for {service_title} booked successfully!"
        )

    # Get provider appointments
    provider_appointments = Appointment.objects.filter(
        availability__provider=request.user
    ).order_by("availability__date", "availability__start_time")

    # Get client appointments
    client_appointments = Appointment.objects.filter(
        client=request.user
    ).order_by(
        "availability__date", "availability__start_time"
    )

    return render(
        request,
        "skillflow/appointments.html",
        {
            "provider_appointments": provider_appointments,
            "client_appointments": client_appointments,
        },
    )


@login_required
def manage_schedule(request, service_id):
    """
    Handles service provider schedule management.
    POST: Creates new availability time slot
    GET: Displays schedule management interface

    Includes validation for:
    - Overlapping time slots
    - Valid dates and times

    Shows both available time slots and upcoming appointments.
    Uses transaction management for data consistency.
    """
    service = get_object_or_404(Service, id=service_id, provider=request.user)

    if request.method == "POST":
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            try:
                availability = form.save(commit=False)
                availability.provider = request.user
                availability.service = service

                # Check for overlapping time slots
                overlapping_slots = Availability.objects.filter(
                    provider=request.user,
                    service=service,
                    date=availability.date,
                    is_booked=False,
                ).filter(
                    models.Q(start_time__lt=availability.end_time)
                    & models.Q(end_time__gt=availability.start_time)
                )

                if overlapping_slots.exists():
                    messages.error(
                        request,
                        "This time slot overlaps with an existing schedule."
                    )
                else:
                    availability.save()
                    messages.success(request, "Time slot added successfully!")

                return redirect("manage_schedule", service_id=service_id)

            except IntegrityError:
                messages.error(request, "This exact time slot already exists.")
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = AvailabilityForm()

    # Source Links:
    # https://forum.djangoproject.com/t/timezone-warning-from-date-filtering-via-the-orm/11776
    # https://www.w3schools.com/django/ref_lookups_gte.php
    availabilities = Availability.objects.filter(
        service=service, date__gte=timezone.now().date()
    ).order_by("date", "start_time")

    appointments = Appointment.objects.filter(
        availability__service=service,
        availability__date__gte=timezone.now().date()
    ).order_by(
        "availability__date", "availability__start_time"
    )

    context = {
        "form": form,
        "service": service,
        "availabilities": availabilities,
        "appointments": appointments,
        "current_date": timezone.now().date(),
    }

    return render(request, "skillflow/manage_schedule.html", context)


@login_required
def delete_availability(request, service_id, availability_id):
    """
    Deletes a specific availability time slot for a service.

    Args:
        request: The HTTP request object
        service_id: ID of the service the availability belongs to
        availability_id: ID of the availability slot to delete

    Requirements:
        - User must be authenticated (enforced by @login_required)
        - User must be the provider of the service
        - Availability slot must not be booked

    Returns:
        Redirects to manage_schedule view after successful deletion or error
    """
    availability = get_object_or_404(
        Availability,
        id=availability_id,
        service__id=service_id,
        provider=request.user
    )

    if request.method == "POST":
        if availability.is_booked:
            messages.error(request, "Cannot delete a booked time slot.")
        else:
            availability.delete()
            messages.success(request, "Time slot deleted successfully.")

    return redirect("manage_schedule", service_id=service_id)


@login_required
def update_appointment_status(request, appointment_id):
    """
    Updates the status of an appointment (confirm or cancel).

    Args:
        request: The HTTP request object
        appointment_id: ID of the appointment to update

    Requirements:
        - User must be authenticated (enforced by @login_required)
        - User must be either the provider or client of the appointment
        - For cancellations within 24 hours, enforces cancellation policy

    Workflow:
        1. Verifies user permissions
        2. Checks cancellation time window if applicable
        3. Updates appointment status using database transaction
        4. Updates related availability booking status
        5. Sends success/error message

    Returns:
        Redirects to appointments view after status update
    """
    appointment = get_object_or_404(Appointment, id=appointment_id)

    is_provider = appointment.availability.provider == request.user
    is_client = appointment.client == request.user

    if not (is_provider or is_client):
        raise PermissionDenied

    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in ["confirmed", "cancelled"]:
            # Cancellation time window check
            if new_status == "cancelled":
                # Calculate time until appointment
                # https://docs.djangoproject.com/en/5.1/topics/i18n/timezones/
                current_datetime = timezone.now()
                appointment_datetime = timezone.make_aware(
                    datetime.combine(
                        appointment.availability.date,
                        appointment.availability.start_time,
                    )
                )
                time_until_appointment = (
                    appointment_datetime - current_datetime
                )

                # Check if less than 24 hours until appointment
                if (
                    time_until_appointment.total_seconds() < 24 * 3600
                ):  # 24 hours in seconds
                    messages.error(
                        request,
                        "Appointments must be cancelled at least 24 hours "
                        "in advance as per our cancellation policy.",
                    )
                    return redirect("appointments")

            with transaction.atomic():
                old_status = appointment.status
                appointment.status = new_status
                appointment.save()

                # If appointment is cancelled, free the slot
                if new_status == "cancelled":
                    availability = appointment.availability
                    availability.is_booked = False
                    availability.save()

                # Prepare appropriate message
                if new_status == "cancelled":
                    msg = "Appointment cancelled successfully."
                else:
                    msg = "Appointment confirmed successfully."
                messages.success(request, msg)

    return redirect("appointments")


def service_detail(request, service_id):
    """
    Displays detailed information about a specific service.

    Args:
        request: The HTTP request object
        service_id: ID of the service to display

    Context:
        - service: Service object with full details
        - provider_profile: UserProfile object of the service provider

    Returns:
        Renders service_detail.html template with service information
    """
    # https://docs.djangoproject.com/en/5.1/topics/http/shortcuts/#get-object-or-404
    service = get_object_or_404(Service, id=service_id)
    # Get the provider's service and profile
    provider_profile = UserProfile.objects.get(user=service.provider)
    return render(
        request,
        "skillflow/service_detail.html",
        {"service": service, "provider_profile": provider_profile},
    )


def cancellation_policy(request):
    """
    Displays the platform's cancellation policy page.

    Returns:
        Renders cancellation_policy.html template
    """
    return render(request, "skillflow/cancellation_policy.html")


def how_it_works(request):
    """
    Displays the platform's how-to guide and information page.

    Returns:
        Renders how_it_works.html template
    """
    return render(request, "skillflow/how_it_works.html")


def help_center(request):
    """
    Displays the platform's help center and support information.

    Returns:
        Renders help_center.html template
    """
    return render(request, "skillflow/help_center.html")


def legal(request):
    """
    Displays the platform's legal information,
    terms of service, and privacy policy.

    Returns:
        Renders legal.html template
    """
    return render(request, "skillflow/legal.html")


def user_info(request, service_id):
    """
    Displays public profile information for a service provider.

    Args:
        request: The HTTP request object
        service_id: ID of the service to get provider information from

    Context:
        - provider_profile: UserProfile object
        with provider's public information

    Returns:
        Renders user_info.html template with provider information
    """
    service = get_object_or_404(Service, id=service_id)
    provider_profile = get_object_or_404(UserProfile, user=service.provider)
    return render(
        request,
        "skillflow/user_info.html",
        {"provider_profile": provider_profile}
    )


def bad_request(request, exception=None):
    """
    Custom 400 error handler.
    """
    return render(request, 'skillflow/400.html', status=400)


def permission_denied(request, exception=None):
    """
    Custom 403 error handler.
    """
    return render(request, 'skillflow/403.html', status=403)


def page_not_found(request, exception=None):
    """
    Custom 404 error handler.
    """
    return render(request, 'skillflow/404.html', status=404)


def server_error(request):
    """
    Custom 500 error handler.
    """
    return render(request, 'skillflow/500.html', status=500)
