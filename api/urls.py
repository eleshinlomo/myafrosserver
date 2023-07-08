from . import views 
from django.urls import path, include



urlpatterns = [
    path('', include('agent.urls')),
    path('', include('user.urls')),
     
      
]