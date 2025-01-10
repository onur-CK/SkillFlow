from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserProfileForm, ServiceForm, AvailabilityForm, AppointmentForm 
from .models import UserProfile, Service, Availability, Appointment
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
import logging
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.utils import timezone

logger = logging.getLogger(__name__)

def about_us(request):
    return render(request, 'skillflow/about_us.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("Form submitted:", request.POST)  # Debug print
        if form.is_valid():
            print("Form is valid")  # Debug print
            user = form.save()
            # Create UserProfile for the new user
            UserProfile.objects.create(user=user)
            auth_login(request, user)
            return redirect('index')
        else:
            print("Form errors:", form.errors)  # Debug print
    else:
        form = SignUpForm()
    return render(request, 'skillflow/sign_up.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
    return render(request, 'skillflow/login.html')

        
@login_required
def index(request):
    category = request.GET.get('category')
    if category:
        services = Service.objects.filter(category=category).order_by('created_at')
    else:
        services = Service.objects.all().order_by('created_at')
    return render(request, 'skillflow/index.html', {
        'services': services,
        'active_category': category
    })

def service(request):
    return render(request, 'skillflow/service.html')

@login_required
def edit_profile(request):
    # Get the profile
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('edit_profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'skillflow/edit_profile.html', {
        'form': form,
        'profile': profile
    })
    
@login_required
def manage_account(request):
    return render(request, 'skillflow/manage_account.html')\

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('about_us')
    return redirect('manage_account')

def logout_view(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('about_us')
    return render(request, 'skillflow/logout.html')

def home(request):
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'skillflow/about_us.html')

@login_required
def service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.provider = request.user
            service.save()
            messages.success(request, 'Service listed successfully!')
            return redirect('index')
    else:
        form = ServiceForm()
    return render(request, 'skillflow/service.html', {'form': form})

def category_services(request, category):
    services = Service.objects.filter(category=category).order_by('created_at')
    return render(request, 'skillflow/index.html', {
        'services': services,
        'active_category': category
    })

@login_required
def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    
    # Check if the current user is the service provider
    if service.provider != request.user:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service updated successfully!')
            return redirect('index')
    else:
        form = ServiceForm(instance=service)

    return render(request, 'skillflow/edit_service.html', {
        'form': form,
        'service': service
    })

@login_required
def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if service.provider != request.user:
        raise PermissionDenied
    
    if request.method == 'POST':
        service.delete()
        messages.success(request, 'Service deleted successfully!')
        return redirect('my_services')
    
    return render(request, 'skillflow/delete_service.html', {'service': service})
    
@login_required
def my_services(request):
    # Django date query from newest to oldest link source: https://stackoverflow.com/questions/30314741/django-date-query-from-newest-to-oldest
    user_services = Service.objects.filter(provider=request.user).order_by('-created_at')
    return render(request, 'skillflow/my_services.html', {
        'user_services': user_services
    })

@login_required 
def provider_availability(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.provider = request.user
            availability.service = service
            availability.save()
            return redirect('manage_availability', service_id=service_id)
    else:
        form = AvailabilityForm()
    
    availabilities = Availability.objects.filter(
        provider=request.user,
        service=service,
        is_booked=False
    ).order_by('date', 'start_time')
    
    return render(request, 'skillflow/availability.html', {
        'form': form,
        'service': service,
        'availabilities': availabilities
    })


@login_required
def book_appointment(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    
    if request.method == 'POST':
        availability_id = request.POST.get('availability')
        availability = get_object_or_404(Availability, id=availability_id)

        # Check if the availability is already booked
        if availability.is_booked:
            messages.error(request, 'Sorry, this time slot has already been booked.')
            return redirect('book_appointment', service_id=service_id)
        
        # Check if trying to book own service
        if service.provider == request.user:
            messages.error(request, 'You cannot book your own service.')
            return redirect('book_appointment', service_id=service_id)
    
        try:
            # Use transaction.atomic() to ensure database consistency
            # Transaction source links: https://www.geeksforgeeks.org/transaction-atomic-with-django/
            # https://docs.djangoproject.com/en/5.1/topics/db/transactions/
            from django.db import transaction
            with transaction.atomic():
                appointment = Appointment.objects.create(
                    availability=availability,
                    client=request.user
                )
                availability.is_booked = True
                availability.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('view_appointments')
        except Exception as e:
            messages.error(request, 'There was an error booking the appointment. Please try again.')
            return redirect('book_appointment', service_id=service_id)

    # GET request handling
    availabilities = Availability.objects.filter(
        service=service,
        is_booked=False,
        # date__gte source links: https://forum.djangoproject.com/t/timezone-warning-from-date-filtering-via-the-orm/11776
        # https://www.w3schools.com/django/ref_lookups_gte.php
        date__gte=timezone.now().date()  # Only show future dates
    ).order_by('date', 'start_time')
    
    return render(request, 'skillflow/book_appointment.html', {
        'service': service,
        'availabilities': availabilities
    })
    

@login_required
def view_appointments(request):
    # Providers
    provider_appointments = Appointment.objects.filter(
        availability__provider=request.user
    ).order_by('availability__date', 'availability__start_time')

    # Clients
    client_appointments = Appointment.objects.filter(
        client=request.user
    ).order_by('availability__date', 'availability__start_time')
    
    
    return render(request, 'skillflow/appointments.html', {
        'provider_appointments': provider_appointments,
        'client_appointments': client_appointments
    })

@login_required
def manage_schedule(request, service_id):
    service = get_object_or_404(Service, id=service_id, provider=request.user)
    schedules = WeeklySchedule.objects.filter(service=service)
    
    if request.method == 'POST':
        form = WeeklyScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.provider = request.user
            schedule.service = service
            schedule.save()

            # Generate availabilities for the next few weeks
            schedule.create_availabilities()
            
            messages.success(request, 'Weekly schedule updated successfully!')
            return redirect('manage_schedule', service_id=service_id)
    else:
        form = WeeklyScheduleForm()
    
    # Get upcoming appointments
    appointments = Appointment.objects.filter(
        availability__service=service,
        availability__date__gte=timezone.now().date()
    ).order_by('availability__date', 'availability__start_time')
    
    return render(request, 'skillflow/manage_schedule.html', {
        'form': form,
        'service': service,
        'schedules': schedules,
        'appointments': appointments
    })


@login_required
def delete_schedule(request, service_id, schedule_id):
    schedule = get_object_or_404(WeeklySchedule, id=schedule_id, service__id=service_id, provider=request.user)
    if request.method == 'POST':
        schedule.delete()
        messages.success(request, 'Schedule deleted successfully.')
    return redirect('manage_schedule', service_id=service_id)