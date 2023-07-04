from . import views
from django.urls import path

urlpatterns = [
    path('addmember/', views.add_member, name='add_member')
]