from django.urls import path, include
from news.views import new, create, detail

urlpatterns = [
    path('', new, name='news'),
    path('create/', create, name = 'create'),
    path('detail/<int:id>', detail, name='detail'),
   
]