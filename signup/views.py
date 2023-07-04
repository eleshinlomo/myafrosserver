from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

@method_decorator(csrf_protect, name='dispatch')
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        greeting = f" Hello {username}"
        return JsonResponse({'greeting': greeting})
    else:
        return None

# Create your views here.
