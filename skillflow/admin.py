from django.contrib import admin
from .models import UserProfile, Service, Availabiltiy, Appointment

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email')
    search_fields = ('user__username', 'first_name', 'last_name', 'email')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'provider', 'hourly_rate', 'created_at')
    list_filter = ('category', 'created')
    search_fields = ('title', 'description', 'provider__username')
