from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .models import SearchHistory
import requests

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    weather = None
    if request.method == 'POST':
        city = request.POST['city']
        api_key = '5285659efbd91a6e2b1a7936000a7ca0'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
        response = requests.get(url).json()
        if response.get('main'):
            weather = {
                'city': city,
                'temperature': response['main']['temp'],
                'description': response['weather'][0]['description'],
            }
            SearchHistory.objects.create(
                user=request.user,
                city=city,
                temperature=weather['temperature'],
                description=weather['description']
            )
        else:
            messages.error(request, 'City not found!')
    return render(request, 'main.html', {'weather': weather})

@login_required
def history(request):
    searches = SearchHistory.objects.filter(user=request.user).order_by('-search_date')
    return render(request, 'history.html', {'searches': searches})

