from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json

@api_view(['GET'])
def getData(request):
    data = {
        'name': 'John Doe',
        'age': 25,
        'is_student': True
    }
    return Response(data)

# Print data posted to the server
@api_view(['POST'])
def postData(request):
    # Pretty print the request body
        request_body = json.loads(request.body)
        pretty_request_body = json.dumps(request_body, indent=4)
        print(pretty_request_body)
        
        # Define response
        response = JsonResponse(
            {
                'message': 'Workflow and catalog successfully recieved'
            }, 
            status=200)
        return response