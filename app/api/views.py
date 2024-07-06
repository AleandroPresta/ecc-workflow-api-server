from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
import logging

# Print data posted to the server
@api_view(['POST'])
def process_post_data(request):
    logging.info("API Called: process_post_data")
    # Recieve data from POST request
    request_body = json.loads(request.body)
    workflow = request_body[0]
    
    catalog = request_body[1]
    
    result = None # TODO add implementation using Strategy Pattern
    # pretty_request_body = json.dumps(request_body, indent=4)
        
    # Define response
    response = JsonResponse(
        {
            'message': 'Workflow and catalog successfully recieved',
            'result': result
        }, 
        status=200)
    
    logging.info("API Finished: sent response to client")
    logging.debug(f"Response: {response}")
    
    return response