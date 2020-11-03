<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
=======
>>>>>>> origin/main
from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('women/', views.women, name='women'),
    path('men/', views.men, name='men'),
    path('girls/', views.girls, name='girls'),
    path('boys/', views.boys, name='boys'),
]
<<<<<<< HEAD

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
>>>>>>> origin/main
