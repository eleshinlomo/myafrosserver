from . import views 
from django.urls import path

urlpatterns = [
    path('api/', views.find_all, name='find_all'),
    path('api/<str:pk>/', views.find_one, name='find_one'),
    
]