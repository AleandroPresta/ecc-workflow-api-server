def compare_workflow_and_catalog(workflow, catalog):
    """
    Compare a workflow and a catalog
    """
    return find_feasible_solution(workflow, catalog)

def find_feasible_solution(workflow, catalog):
    solution = {}

    for node in workflow['nodes']:
        if node['type'] != 'Device':
            best_service = None
            best_service_params = {}
            for service in catalog['services']:
                if service['type'] == node['type']:
                    # Convert parameters to integers for comparison
                    workflow_params = {param: int(value) for param, value in node['parameters'].items()}
                    service_params = {param: int(value) for param, value in service['parameters'].items()}
                    
                    # Check if service parameters are greater than or equal to node parameters
                    greater_params = all(service_params.get(param, 0) >= workflow_params.get(param, 0) for param in workflow_params)
                    if greater_params:
                        # Check if service parameters are less than or equal to node parameters
                        if not best_service or len(service_params) > len(best_service_params):
                            best_service = service
                            best_service_params = service_params

            if best_service:
                solution[node['id']] = best_service

    return solution