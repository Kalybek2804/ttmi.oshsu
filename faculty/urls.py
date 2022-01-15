from django.urls import path
from faculty.views import *
from django.views import generic

urlpatterns = [
    path('', faculty, name='faculty'),
    path('programmer/', programmer, name='programmers'),
    path('journalism/', journalism, name='journalismes'),
    path('economika/', economika, name='economikas'),
    path('tourism/', tourism, name='tourismes'),
    path('teachers/', TeacherListView.as_view(), name='teachers'),
    path('lessons/', LessonListView.as_view(), name='lessons'),
    
    
   
]