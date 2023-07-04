from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Member
from rest_framework.decorators import permission_classes, api_view
from rest_framework import permissions
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from api.serializer import MemberSerializer



# Create your views here.
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
@csrf_exempt
def add_member(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    member = Member(username=username, password=password, email=email)
    member.save()

    serializer = MemberSerializer(member)

    return Response(serializer.data)