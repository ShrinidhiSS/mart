from django.shortcuts import render

from myapp.models import Product


def home(request):
    return render(request, 'myapp/home.html')


def men(request):
    men = Product.objects.filter(category_name__exact='Men')
    return render(request, 'myapp/men.html', {'men': men})


def women(request):
    women = Product.objects.filter(category_name__exact='Women')
    return render(request, 'myapp/women.html', {'women': women})


def girls(request):
    girls = Product.objects.filter(category_name__exact='Girls')
    return render(request, 'myapp/girls.html', {'girls': girls})


def boys(request):
    boys = Product.objects.filter(category_name__exact='Boys')
    return render(request, 'myapp/boys.html', {'boys': boys})


def detail(request, id):
    details = Product.objects.filter(id=id)
    return render(request, 'myapp/detail.html', {'details': details})


def cart(request):
    return render(request, 'myapp/cart.html')
