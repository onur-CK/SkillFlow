"""
URL configuration for skillflow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .models import Service
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.conf import settings


# URL configuration for the SkillFlow project.
# Defines URL patterns and maps them to corresponding views.

urlpatterns = [
    # Admin Interface URLs
    path("admin/", admin.site.urls),
    # Core navigation URLs
    path("", views.home, name="home"),  # Landing page
    path("index/", views.index, name="index"),  # Main dashboard
    path("about-us", views.about_us, name="about_us"),  # About page
    # Authentication URLs
    path("sign-up/", views.sign_up, name="sign_up"),  # User registration
    path("login/", views.login, name="login"),  # Login page
    path("logout/", views.logout_view, name="logout"),  # Logout handler
    # Profile Management URLs
    path("profile/edit/", views.edit_profile, name="edit_profile"),  # Edit profile
    path(
        "profile/manage/", views.manage_account, name="manage_account"
    ),  # Account management
    path(
        "profile/delete/", views.delete_account, name="delete_account"
    ),  # Account deletion
    # Service Management URLs
    path("service/", views.service, name="service"),  # Create service
    path(
        "service/<int:service_id>/edit/", views.edit_service, name="edit_service"
    ),  # Edit service
    path(
        "service/<int:service_id>/delete/", views.delete_service, name="delete_service"
    ),  # Delete service
    path(
        "profile-services", views.my_services, name="my_services"
    ),  # List user's services
    # Category filtering
    path("category/<str:category>/", views.category_services, name="category_services"),
    # Scheduling and appointment URLs
    path(
        "service/<int:service_id>/schedule/",
        views.manage_schedule,
        name="manage_schedule",
    ),
    path(
        "service/<int:service_id>/schedule/delete/<int:availability_id>/",
        views.delete_availability,
        name="delete_availability",
    ),
    path("appointments/", views.view_appointments, name="appointments"),
    path(
        "service/<int:service_id>/book/",
        views.book_appointment,
        name="book_appointment",
    ),
    path(
        "appointment/<int:appointment_id>/update",
        views.update_appointment_status,
        name="update_appointment_status",
    ),
    # Additional pages
    path(
        "service/<int:service_id>/detail/", views.service_detail, name="service_detail"
    ),
    path("cancellation-policy/", views.cancellation_policy, name="cancellation_policy"),
    path("how-it-works/", views.how_it_works, name="how_it_works"),
    path("help-center/", views.help_center, name="help_center"),
    path("legal/", views.legal, name="legal"),
    path("user/<int:service_id>/user-info/", views.user_info, name="user_info"),
    path("check-ssl/", views.check_ssl_settings, name="check_ssl"),
    path("check-static/", views.check_static_settings, name="check_static"),
]
