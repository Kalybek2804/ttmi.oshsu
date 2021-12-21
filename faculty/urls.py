from django.urls import path, include
from faculty.views import faculty, programmer, journalism, economika, tourism, teachers, lessons

urlpatterns = [
    path('', faculty, name='faculty'),
    path('programmer/', programmer, name='programmers'),
    path('journalism/', journalism, name='journalismes'),
    path('economika/', economika, name='economikas'),
    path('tourism/', tourism, name='tourismes'),
    path('teachers/', teachers, name='teachers'),
    path('lessons/', lessons, name='lessons'),
    
   
]