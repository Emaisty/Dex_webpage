from django.shortcuts import render


def index(request):
    content = {1: 1}
    return render(request, 'index.html', content)
