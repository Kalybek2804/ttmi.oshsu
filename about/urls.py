from django.urls import path
from about.views import *

urlpatterns = [
    path('', about, name='about'),
    path('contact/', maps, name='maps'),
    
   
]

