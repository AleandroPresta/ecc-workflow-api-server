import sys
sys.path.append('app/api')

from lib.inequalities_utils import pretty_print_solution

'''
    This function takes a workflow and categorizes the nodes by their type.
    Example of usage:
    workflow = {
        'nodes': [
            {
                'name': 'Storage 1',
                'id': 1,
                'type': 'Storage',
                ...
            },
            {
                'name': 'Storage 2',
                'id': 2,
                'type': 'Storage',
                ...
            },
            {
                'name': 'Computation 1',
                'id': 3,
                'type': 'Computation',
                ...
            }
        ]
    }
    
    returns:
    {
        'Storage': [
            {
                'name': 'Storage 1', 
                'id': 1, 
                'type': 'Storage'
            },
            {
                'name': 'Storage 2',
                'id': 2, 
                'type': 'Storage'
            }
        ], 
        'Computation': [
            {
                'name': 'Computation 1',
                'id': 3, 
                'type': 'Computation'
            }
        ]
    }
    
'''
def categorize_nodes_by_type(workflow):
    categorized = {}
    for node in workflow['nodes']:
        node_type = node['type']
        if node_type not in categorized:
            categorized[node_type] = { 'nodes' : [] }
        categorized[node_type]['nodes'].append(node)
    return categorized

'''
    This function takes a catalog and categorizes the services by their type.
    Example of usage:
    catalog = {
        'services': [
            {
                'name': 'Service 0',
                'id': 0,
                'type': 'Computation',
                ...
            },
            {
                'name': 'Service 1',
                'id': 1,
                'type': 'Storage',
                ...
            }
        ]
    }
    
    returns:
    {
        'Computation': [
            {
                'name': 'Service 0',
                'id': 0,
                'type': 'Computation'
            }
        ],
        'Storage': [
            {
                'name': 'Service 1',
                'id': 1,
                'type': 'Storage'
            }
        ]
    }
'''
def categorize_catalog_by_type(catalog):
    categorized = {}
    for service in catalog['services']:
        service_type = service['type']
        if service_type not in categorized:
            categorized[service_type] = { 'services' : [] }
        categorized[service_type]['services'].append(service)
    return categorized