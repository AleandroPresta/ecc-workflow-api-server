# views.py
from django.http import JsonResponse

def homepage(request):
    # Handle GET request
    if request.method == 'GET':
        return JsonResponse(
            {
                'message': 'Welcome to the homepage of the Django API'
            }, 
            status=200)