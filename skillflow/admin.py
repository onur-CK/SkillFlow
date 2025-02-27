from django.contrib import admin
from .models import UserProfile, Service, Availability, Appointment

# Register UserProfile model with custom admin configuration


@admin.register(UserProfile)
# Source Links for ModelAdmin customization:
# https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#modeladmin-objects
# https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
class UserProfileAdmin(admin.ModelAdmin):
    # Configure which fields are displayed in the user profile list view
    list_display = ("user", "first_name", "last_name", "email")
    # Enable searching through user profiles by username,first name, last name, and email
    # Source Link: https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
    search_fields = ("user__username", "first_name", "last_name", "email")


# Register Service model with custom admin configuration
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    # Configure which fields are displayed in the service list view
    list_display = ("title", "category", "provider", "hourly_rate", "created_at")
    # Add filter options for category and creation date
    # Source for list_filter options: https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter
    list_filter = ("category", "created_at")
    # Enable searching through services by title, description, and provider username
    search_fields = ("title", "description", "provider__username")


# Register Availability model with custom admin configuration
@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    # Configure which fields are displayed in the availability list view
    list_display = (
        "service",
        "provider",
        "date",
        "start_time",
        "end_time",
        "is_booked",
    )
    # Add filter options for booking status and date
    list_filter = ("is_booked", "date")
    # Enable searching through availabilities by provider username and service title
    search_fields = ("provider__username", "service__title")


# Register Appointment model with custom admin configuration
@admin.register(Appointment)
# Source Links for custom admin methods: https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
# https://stackoverflow.com/questions/18108521/django-admin-list-display-method-with-foreign-key
class AppointmentAdmin(admin.ModelAdmin):
    # Configure which fields are displayed in the appointment list view using custom methods
    # Uses custom methods to access nested relationship fields
    list_display = (
        "get_service",
        "get_provider",
        "client",
        "get_date",
        "status",
        "created_at",
    )
    # Add filter options in the admin interface for appointment status and creation date
    list_filter = ("status", "created_at")
    # Enable searching through appointments by service title, client username, and provider username
    search_fields = (
        "availability__service__title",
        "client__username",
        "availability__provider__username",
    )

    # Custom method to get and display the service title
    # Accesses the service title through the availability relationship
    def get_service(self, obj):
        return obj.availability.service.title

    # Source Link: https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#django.contrib.admin.display
    get_service.short_description = "Service"

    # Custom method to display the provider username in the admin list view
    # Accesses the provider username through the availability relationship
    def get_provider(self, obj):
        return obj.availability.provider.username

    get_provider.short_description = "Provider"

    # Custom method to display the appointment date in the admin list view
    # Accesses the date through the availability relationship
    def get_date(self, obj):
        return obj.availability.date

    get_date.short_description = "Date"
