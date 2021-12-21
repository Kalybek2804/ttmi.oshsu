from django.shortcuts import render
from faculty.models import Teacher, Lesson

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



def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'faculty/kafedra/teachers.html', {'teachers': teachers})


def lessons(request):
    lessons = Lesson.objects.all()
    return render(request, 'faculty/kafedra/teachers.html', {'lessons': lessons})
