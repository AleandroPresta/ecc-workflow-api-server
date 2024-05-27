# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def homepage(request):
    # Handle GET request
    if request.method == 'GET':
        return JsonResponse(
            {
                'message': 'GET request recieved'
            }, 
            status=200)
        
    # Handle POST request by printing the request body
    if request.method == 'POST':
        # Pretty print the request body
        request_body = json.loads(request.body)
        pretty_request_body = json.dumps(request_body, indent=4)
        print(pretty_request_body)
        
        # Define response
        response = JsonResponse(
            {
                'message': 'Workflow Recieved'
            }, 
            status=200)
        return response