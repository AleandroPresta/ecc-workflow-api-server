from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
import logging
from .solving_strategy.LLMStrategy import LLMStrategy
from django.urls import path

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
def solve_with_llm(request, model_id):
    logging.info(f"API Called: solve_with_llm with model_id: {model_id}")
    
    request_body = json.loads(request.body)
    
    workflow: dict = request_body[0]
    catalog: dict = request_body[1]
    
    strategy = LLMStrategy()
    
    response = JsonResponse(
        {
            'message': 'Solving with LLM',
            'request_body': strategy.solve(workflow, catalog, model_id)
        }, 
        status=200
    )
    
    return response