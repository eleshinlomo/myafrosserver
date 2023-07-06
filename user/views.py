from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes, api_view
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
@csrf_protect
def create_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return Response({'message': 'You have successfully registered'})
    else:
        return Response({'message': 'Error registering user'})
