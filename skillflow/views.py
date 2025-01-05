from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserProfileForm

def about_us(request):
    return render(request, 'skillflow/about_us.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("Form submitted:", request.POST)  # Debug print
        if form.is_valid():
            print("Form is valid")  # Debug print
            user = form.save()
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
    return render(request, 'skillflow/index.html')

def service(request):
    return render(request, 'skillflow/service.html')

@login_required
def edit_profile(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('edit_profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'skillflow/edit_profile.html', {'form': form})

