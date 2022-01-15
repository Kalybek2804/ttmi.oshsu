from django.db import models
from django.forms import fields, widgets
from news.models import New
from django import forms

class NewForm(forms.ModelForm):

    class Meta:
        model = New
        fields = '__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
        }

