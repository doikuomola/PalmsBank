from django.shortcuts import render

def home(request):
    return render(request, 'banking/home.html')

def login(request):
    return render(request, 'banking/login.html')

def profile(request):
    return render(request, 'registration/profile.html')

def contact(request):
    return render(request, 'banking/contact.html')

def about(request):
    return render(request, 'banking/about.html')