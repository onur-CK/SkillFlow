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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('about-us', views.about_us, name='about_us'),

    # Authentication URLs
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Profile Management URLs
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/manage/', views.manage_account, name='manage_account'),
    path('profile/delete/', views.delete_account, name='delete_account'),

    # Service URLs
    path('service/', views.service, name='service'),
    path('service/<int:service_id>/edit/', views.edit_service, name='edit_service'),
    path('service/<int:service_id>/delete/', views.delete_service, name='delete_service'),
    path('profile-services', views.my_services, name='my_services'),
    
    path('category/<str:category>/', views.category_services, name='category_services'),

    # Availability and Appointments
    path('service/<int:service_id>/schedule/', views.manage_schedule, name='manage_schedule'),
    path('service/<int:service_id>/schedule/delete/<int:availability_id>/', views.delete_availability, name='delete_availability'),
    path('appointments/', views.view_appointments, name='appointments'),
    path('service/<int:service_id>/book/', views.book_appointment, name='book_appointment'),
    path('appointment/<int:appointment_id>/update', views.update_appointment_status, name='update_appointment_status'),
]
