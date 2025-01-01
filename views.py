from django.shortcuts import render

def index(request):
    return render(request, 'edit_profile.html')