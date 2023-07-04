from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .serializer import AgentSerializer
from ai.models import Agent

# Create your views here.
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def find_all(request):
    
        agents = Agent.objects.all()
        serializer = AgentSerializer(agents, many = True)
        return Response(serializer.data)

# Create your views here.
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def find_one(request, pk):
    
        agent = Agent.objects.get(id=pk)
        serializer = AgentSerializer(agent, many = False)
        return Response(serializer.data)





   
