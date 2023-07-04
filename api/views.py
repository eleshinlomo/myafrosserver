from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt

# serializers
from .serializer import AgentSerializer
from .serializer import MemberSerializer

# models
from member.models import Member
from ai.models import Agent

# object destructuring

# find all users
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_users(request):
       members = Member.objects.all()
       serializer = MemberSerializer(members, many = True)
       return Response(serializer.data)
       

def get_user(request, pk):
       member = Member.objects.get(id=pk)
       serializer = MemberSerializer(member, many = False)
       return Response(serializer.data)
       



# find all ai agents
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def find_all(request):
        agents = Agent.objects.all()
        serializer = AgentSerializer(agents, many = True)
        return Response(serializer.data)

# find one ai agent.
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def find_one(request, pk):
        agent = Agent.objects.get(id=pk)
        serializer = AgentSerializer(agent, many = False)
        return Response(serializer.data)










   
