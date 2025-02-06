from django.contrib import admin
from .models import UserProfile, Service, Availability, Appointment

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email')
    search_fields = ('user__username', 'first_name', 'last_name', 'email')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'provider', 'hourly_rate', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description', 'provider__username')

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('service', 'provider', 'date', 'start_time', 'end_time', 'is_booked')
    list_filter = ('is_booked', 'date')
    search_fields = ('provider__username', 'service__title')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('get_service', 'get_provider', 'client', 'get_date', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('availability__service__title', 'client__username', 'availability__provider__username')

    def get_service(self, obj):
        return obj.availability.service.title
    get_service.short_description = 'Service'

    def get_provider(self, obj):
        return obj.availability.provider.username
    get_provider.short_description = 'Provider'

    def get_date(self, obj):
        return obj.availability.date
    get_date.short_description = 'Date'

    