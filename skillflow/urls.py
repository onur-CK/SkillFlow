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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('home/', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'),
    path('', views.about_us, name='about_us'),
]
