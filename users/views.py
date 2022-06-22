from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth import login, authenticate
from base.models import Task


def profile(request, id):
    user = User.objects.get(id = id)
    tasks = Task.objects.all()
    context = {
        'tasks' : tasks,
        'user' : user
        }

    return render(request, 'profile.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            try:
                user = User.objects.create(username=username)
                user.set_password(password1)
                user.save()
                return redirect('tasks')
            except:
                messages.error(request, 'Неправильные данные')
        else:
            messages.error(request, 'Пароли отличаются')

    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('tasks')
        except:
            messages.error(request, "Неправильный логин или пароль")

    return render(request, 'login.html')

    

