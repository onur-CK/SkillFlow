from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile


def edit_profile(request):
    return render(request, 'skillflow/edit_profile.html')

def index(request):
    return render(request, 'skillflow/index.html')

def login(request):
    return render(request, 'skillflow/login.html')

def service(request):
    return render(request, 'skillflow/service.html')

def about_us(request):
    return render(request, 'skillflow/about_us.html')

def sign_up(request):
    # Check if the request is a POST request (form submitted by the user).
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['confirm-password']
        
        if password != password_confirm:
            return redirect('sign_up')
        
        if User.objects.filter(username=username).exists():
            return redirect('sign up')
    
        # Create a new user with the given username and password.
        user = User.objects.create_user(username=username, password=password)
        # Create a UserProfile instance for the newly created user.
        UserProfile.objects.create(user=user)
        
    return render(request, 'skillflow/sign_up.html') 
    
        
        


        


