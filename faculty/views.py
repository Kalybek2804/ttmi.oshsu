from django.shortcuts import render
from django.db import models
from django.urls.base import reverse_lazy
from faculty.models import *
from faculty.forms import *
from django.views import generic


   

def faculty(request):
    return render(request, 'faculty/faculty.html')


def programmer(request):
    return render(request, 'faculty/programmers.html')

def journalism(request):
    return render(request, 'faculty/journalism.html')


def economika(request):
    return render(request, 'faculty/economika.html')


def tourism(request):
    return render(request, 'faculty/tourism.html')



# def teachers(request):
#     teachers = Teacher.objects.all()
#     return render(request, 'faculty/kafedra/teachers.html', {'teachers': teachers})


# def lesson(request):
#     lessons = Lesson.objects.all()
#     return render(request, 'faculty/kafedra/teachers.html', {'lessons': lessons})



class TeacherListView(generic.ListView):
    queryset = Teacher.objects.all()
    model = Teacher
    template_name = 'faculty/kafedra/teachers.html'
    context_object_name = "teachers"

    

class LessonListView(generic.ListView):
    queryset = Lesson.objects.all()
    model = Lesson
    template_name = 'faculty/kafedra/teachers.html'
    context_object_name = "lessons"