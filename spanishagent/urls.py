from . import views
from django.urls import path

urlpatterns = [
    path('translate_to_spanish/', views.translate_to_spanish, name='translate_to_spanish' )
]