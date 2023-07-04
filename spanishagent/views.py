from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view


from rest_framework import permissions
import os
import openai

# Create your views here.


openai.api_key = os.getenv("OPENAI_API_KEY", None)
@csrf_exempt
@api_view(['POST', 'GET'])
@permission_classes([permissions.AllowAny])
def translate_to_spanish(request):
    
    if request.method == 'POST' and openai.api_key is not None:
        user_input = request.data.get('user_input')
        prompt = f" translate to spanish: {user_input}"

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=20,
        )
        generated_text = response.choices[0].text.strip()

        return Response({
            'generated_text': generated_text,
            
            })
    else:
        return Response({
            'response': 'Request was not successful buddy'
            })
