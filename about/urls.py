from django.urls import path, include
from about.views import about, maps

urlpatterns = [
    path('', about, name='about'),
    path('contact/', maps, name='maps'),
    
   
]