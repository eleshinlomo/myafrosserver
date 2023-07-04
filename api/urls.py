from . import views 
from django.urls import path


urlpatterns = [
    path('agents/', views.find_all, name='find_all'),
    path('agent/<str:pk>/', views.find_one, name='find_one'),
    
    
]