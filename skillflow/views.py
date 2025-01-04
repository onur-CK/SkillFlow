from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

def login(request):
    return render(request, 'skillflow/login.html')

def about_us(request):
    return render(request, 'skillflow/about_us.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Automatically log in user after signup
            return redirect('index')  # Redirect to index page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'skillflow/sign_up.html', {'form': form})
        
    return render(request, 'skillflow/sign_up.html') 
    
  
@login_required
def index(request):
    return render(request, 'skillflow/index.html')

def service(request):
    return render(request, 'skillflow/service.html')

def edit_profile(request):
    return render(request, 'skillflow/edit_profile.html')

