from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import logging
from .models import Appliance

logger = logging.getLogger(__name__)
from .forms import ApplianceForm

# Home view
def home(request):
    return render(request, 'home.html')

# Login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Redirect to profile page after successful login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

# Logout view
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# Register view
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already registered')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Registration successful! Please log in.')
                print("User created successfully, redirecting to login...")  # Debugging
                return redirect('login')  # Redirect to login page after successful registration
        else:
            messages.error(request, 'Passwords do not match')
    
    return render(request, 'register.html')

# Profile view
def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if user is not authenticated
    ApplianceForm = request.session.get('ApplianceForm', 0)  # Get energy usage from session
    return render(request, 'profile.html', {'user': request.user, 'ApplianceForm': ApplianceForm})

def calculator(request):
    if request.method == 'POST':
        form = ApplianceForm(request.POST)
        if form.is_valid():
            appliances = form.save()
            appliances.monthly_usage = appliances.monthly_usage()
            appliances.save()
            return redirect('profile')
    else:
        form = ApplianceForm()
    return render(request, 'calculator.html')

def energyusage(request):
    return render(request, 'energyusage.html')

def costsavings(request):
    return render(request, 'costsavings.html')

def sustainability(request):
    return render(request, 'sustainability.html')

# Create your views here.
