from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect


def index(request):
    if request.user.is_authenticated:
        content = {'auth': 1,
                   'name': request.user.username}
    else:
        content = {'auth': 0}
    return render(request, 'index.html', content)


@csrf_protect
def log_in(request):
    data = request.POST.dict()
    user = authenticate(username=data['name'], password=data['password'])
    login(request, user)
    return redirect('/')


@csrf_protect
def log_out(request):
    logout(request)
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
