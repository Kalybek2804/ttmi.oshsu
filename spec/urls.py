from django.urls import path, include
from spec.views import *

urlpatterns = [
   path('', spec_programmer, name='spec_programmer'),
   
]





