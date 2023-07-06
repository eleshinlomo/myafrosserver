from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt

# serializers
from .serializer import AgentSerializer


# models
from ai.models import Agent

# object destructuring


       



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










   
