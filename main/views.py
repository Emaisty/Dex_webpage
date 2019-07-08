from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('/login')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        data = request.POST.dict()
        # check
        return render(request, 'index.html')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        data = request.POST.dict()
        # create
        return render(request, 'index.html')
