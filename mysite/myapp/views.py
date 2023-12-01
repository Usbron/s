from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product

def index(request):
    items = Product.objects.all()
    context = {
        'items':items
    }
    return render(request, "myapp/index.html", context)

def indexItem(request, my_id):
    item = Product.objects.get(id=my_id)
    context = {
        'item': item
    }
    return render(request, "myapp/detail.html", context)

def register(request):
    if request.method == 'POST': #POST - это один из HTTP-методов, используемых для отправки данных на сервер
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None: #проверяет, успешно ли прошла аутентификация пользователя.
                login(request, user) #выполняет вход пользователя в систему
                return render(request, 'myapp/profile.html')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})

def profile_view(request):
    return render(request, 'myapp/profile.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password) #проверяет правильность комбинации имени пользователя и пароля
        if user is not None: #проверка, успешно ли прошла аутентификация пользователя
            login(request, user) #выполнение входа пользователя в систему
            return render(request, "myapp/profile.html")
        else:
            return render(request, 'myapp/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'myapp/login.html')