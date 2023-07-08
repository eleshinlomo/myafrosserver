from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes, api_view
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from api.serializer import UserSerializer

# Register.
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
@csrf_protect
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    if User.objects.filter(username=username).exists():
        return Response({'message': 'Username already exist in our database'})
    if User.objects.filter(email=email).exists():
        return Response({'message': 'Email already exist in our database'})
    else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return Response({'message': 'You have successfully registered.'})
    



# user login
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
@csrf_protect
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)

    if user is not None:
        login(request, user)
        return Response({'message': 'You are now logged in'})
    else:
        return Response({'message': 'Error with logins'})
    

# get all users
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
@csrf_protect
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response({'users': serializer.data})

