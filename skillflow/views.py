from django.shortcuts import render

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
    if request.metod == 'POST': 


