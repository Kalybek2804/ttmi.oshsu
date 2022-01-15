from django.shortcuts import render
from django.db import models
from django.urls.base import reverse_lazy
from news.models import New
from news.forms import NewForm
from django.views import generic


class NewListView(generic.ListView):
    queryset = New.objects.all()
    model = New
    template_name = 'news/new.html'
    context_object_name = "news"

class NewDetailView(generic.DetailView):
    model = New
    template_name = 'news/detail.html'
    context_object_name = "news"
    
    def get_object(self):
        obj = super().get_object()
        obj.news_view += 1
        obj.save()
        return obj

    










