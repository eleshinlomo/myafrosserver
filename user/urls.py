from . import views
from django.urls import path


urlpatterns = [
path('createuser/', views.create_user, name='create_user'),
path('login/', views.login_user, name='login_user'),
path('users/', views.get_users, name='get_users')
]