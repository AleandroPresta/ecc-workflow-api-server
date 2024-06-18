from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
from .lib.workflow_catalog_evaluator import compare_workflow_and_catalog
import logging

logging.basicConfig(
    level=logging.info,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Print data posted to the server
@api_view(['POST'])
def process_post_data(request):
    logging.info("API Called: process_post_data")
    # Recieve data from POST request
    request_body = json.loads(request.body)
    workflow = request_body[0]
    
    catalog = request_body[1]
    
    result = compare_workflow_and_catalog(workflow, catalog)
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