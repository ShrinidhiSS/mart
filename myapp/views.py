from django.shortcuts import render


def home(request):
    return render(request, 'myapp/home.html')


def men(request):
    return render(request, 'myapp/men.html')


def women(request):
    return render(request, 'myapp/women.html')


def girls(request):
    return render(request, 'myapp/girls.html')


def boys(request):
    return render(request, 'myapp/boys.html')
