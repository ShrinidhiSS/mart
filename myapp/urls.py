from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('women/', views.women, name='women'),
    path('men/', views.men, name='men'),
    path('girls/', views.girls, name='girls'),
    path('boys/', views.boys, name='boys'),
]
