from django.shortcuts import render

def edit_profile(request):
    return render(request, 'skillflow/edit_profile.html')

def index(request):
    return render(request, 'skillflow/index.html')

def login(request):
    return render(request, 'skillflow/login.html')

def service(request):
    return render(request, 'skillflow/service.html')

def sign_up(request):
    return render(request, 'skillflow/sign_up.html')