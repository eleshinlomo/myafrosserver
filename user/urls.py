from . import views
from django.urls import path


urlpatterns = [
path('createuser/', views.create_user, name='create_user')
]