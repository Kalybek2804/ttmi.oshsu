from news.views import *
from django.urls import path


urlpatterns = [
    path('', NewListView.as_view(), name='news'),
    path('detail/<int:pk>', NewDetailView.as_view(), name='detail'),
]






