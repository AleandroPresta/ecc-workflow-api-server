# views.py
from django.http import JsonResponse

def homepage(request):
    if request.method == 'GET':
        return JsonResponse(
            {
                'message': 'OK'
            }, 
            status=200)