from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Member
from rest_framework.decorators import permission_classes, api_view
from rest_framework import permissions
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from api.serializer import MemberSerializer
from django.contrib.auth import authenticate, login



# Create your views here.
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
@csrf_exempt
def add_member(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if Member.objects.filter(username=username).exists():
        return Response({'message': 'Username already exist'})
    
    if Member.objects.filter(email=email).exists():
        return Response({
            'message': 'Email already exist'
        })
    
    else:
        member = Member(username=username, password=password, email=email)
        member.save()
        serializer = MemberSerializer(member)

    return Response({
        'response': serializer.data,
        'message': 'You have successfully registered',
        'status': 'ok'
        })


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
@csrf_exempt
def login_member(request):
    
    
    email = request.data.get('email')
    password = request.data.get('password')
    member = authenticate(request, username=email, password=password)

    if member is not None:
        login(request, member)
        username = member.username
        return Response({'message': f"Hello {username}, You are now logged in"})
    else:
        return Response({'message': "Unable to login"})