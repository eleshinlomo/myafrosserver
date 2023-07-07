from django.shortcuts import render
from django.http import HttpResponse


def test(request):
    return HttpResponse('My Afros Server now running')

# Create your views here.
