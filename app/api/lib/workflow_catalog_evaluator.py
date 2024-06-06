from utils import pretty_print_solution

"""
    Compare a workflow and a catalog
    :param workflow: The workflow to compare
    :param catalog: The catalog to compare
    :return: A dictionary of the services selected for each node in the workflow
"""
def compare_workflow_and_catalog(workflow, catalog):
    return find_feasible_solution(workflow, catalog)

''' 
    Selects services for each node in the workflow. The services selected are the first
    occurences in the catalog that have parameters greater than or equal to the node parameters.
    If a service is selected, it is removed from the catalog and added to the solution.
 '''
def find_feasible_solution(workflow, catalog):
    solution = {}
    # Copy the catalog as available services
    available_services = catalog.copy()

    # Iterate through each node in the workflow
    for node in workflow['nodes']:
        # Check if node is a device (we esclude devices because they have no parameters)
        if node['type'] != 'Device':
            best_service = None
            best_service_params = {}
            # Iterate through each service in the catalog
            for service in available_services['services']:
                # Check if service type matches node type
                if service['type'] == node['type']:
                    # Convert parameters to integers for comparison
                    workflow_params = {param: int(value) for param, value in node['parameters'].items()}
                    service_params = {param: int(value) for param, value in service['parameters'].items()}
                    
                    # greater_params is True if all service parameters are greater than or equal to node parameters
                    greater_params = all(service_params.get(param, 0) >= workflow_params.get(param, 0) for param in workflow_params)
                    
                    if greater_params:
                        # Check if service parameters are less than or equal to node parameters
                        if not best_service or len(service_params) > len(best_service_params):
                            best_service = service
                            best_service_params = service_params
                            
            if best_service:
                # Remove selected service from available services
                available_services['services'].remove(best_service)
                # Add selected service to solution
                solution[node['id']] = best_service
                
    # Check if the solution covers all the services
    print(f'The solution covers {len(solution)} services out of {len(workflow["nodes"])} nodes.')
    if len(solution) != len(workflow['nodes']):
        return None # No solution found
    return solution