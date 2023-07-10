from . import views
from django.urls import path

urlpatterns = [
    path('english/', views.english, name='english')
]