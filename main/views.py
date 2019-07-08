from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('/log_in')


def log_in(request):
    if request.method == "GET":
        return render(request, 'log_in.html')
    else:
        data = request.POST.dict()
        user = authenticate(username=data['name'], password=data['password'])
        login(request, user)
        return redirect('/')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        # check
        data = request.POST.dict()
        name = data['name']
        email = data['email']
        psswd = data['password1']
        print(name, email, psswd)
        user = User.objects.create_user(name, email, psswd)
        user.save()
        return redirect('../log_in')
