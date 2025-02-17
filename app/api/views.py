from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
import logging
from icecream import ic
from .solving_strategy.WorkflowServiceOptimizerFacade import WorkflowServiceOptimizerFacade

@api_view(['GET', 'POST'])
def home(request):
    logging.info("API Called: home")
    response = JsonResponse(
        {
            'message': 'Welcome to the Workflow Service Optimizer API'
        }, 
        status=200
    )
    
    logging.info("API Finished: sent response to client")
    logging.debug(f"Response: {response}")
    
    return response

@api_view(['GET', 'POST'])
def solve_with_llm(request):
    logging.info("API Called: solve_with_llm")
    
    request_body = json.loads(request.body)
    
    response = JsonResponse(
        {
            'message': 'Solving with LLM',
            'request_body': request_body
        }, 
        status=200
    )
    
    return response