from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
import logging
from icecream import ic
from .solving_strategy.WorkflowServiceOptimizerFacade import WorkflowServiceOptimizerFacade

@api_view(['GET','POST'])
def process_post_data(request):
    logging.info("API Called: process_post_data")
    
    request_body = json.loads(request.body)
    ic(request_body)
    workflow = request_body[0]
    catalog = request_body[1]

    distance_function = None
    VERBOSE = False
    facade = WorkflowServiceOptimizerFacade(distance_function=distance_function, VERBOSE=VERBOSE)
    result = facade.findOptimalServices(workflow=workflow, catalog=catalog, solver_type="inequalities")
    ic(result)
    response = JsonResponse(
        {
            'message': 'Workflow and catalog successfully received',
            'result': result
        }, 
        status=200
    )
    
    logging.info("API Finished: sent response to client")
    logging.debug(f"Response: {response}")
    
    return response