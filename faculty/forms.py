from django.db import models
from django.forms import fields, widgets
from faculty.models import *
from django import forms

class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
        }


class LessonForm(forms.ModelForm):

    class Meta:
        models = Lesson
        fields = '__all__'
        widgets = {
            'lesson_name':forms.TextInput(attrs={'class':'form-control'}),
        }