from django.shortcuts import render
from .models import Logo
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages  # Импортируем сообщения

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {username}!')  # Отображаем сообщение об успешном входе
                return redirect('home')  # Перенаправление на главную страницу
            else:
                messages.error(request, 'Неверное имя пользователя или пароль.')  # Отображаем сообщение об ошибке
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')  # Отображаем сообщение об ошибке
    else:
        form = AuthenticationForm()
    logo = Logo.objects.first()
    return render(request, 'login.html', {'form': form, 'logo': logo})

def home(request):
    logo = Logo.objects.first()
    return render(request, 'home.html', {'logo': logo})

def login(request):
    logo = Logo.objects.first()
    return render(request, 'login.html', {'logo': logo})

def wallet(request):
    logo = Logo.objects.first()
    return render(request, 'wallet.html', {'logo': logo})