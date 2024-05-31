from workflow_catalog_evaluator import compare_workflow_and_catalog
import json

def get_sample_data():
    workflow = {
        'nodes': [
            {
                'name': 'Computation 1',
                'id': 1,
                'type': 'Computation',
                'parameters': {'executionTime': 10, 'volumeOfData': 25},
            },
            {
                'name': 'Computation 2',
                'id': 2,
                'type': 'Computation',
                'parameters': {'executionTime': 10, 'volumeOfData': 25},
            }
        ]
    }

    catalog = {
        'services': [
            {
                'name': 'Service 0',
                'id': 0,
                'type': 'Computation',
                'parameters': {'executionTime': '5', 'volumeOfData': '25'},
                'description': 'This is a computation service'
            },
            {
                'name': 'Service 1',
                'id': 1,
                'type': 'Computation',
                'parameters': {'executionTime': '11', 'volumeOfData': '25'},
                'description': 'This is a computation service'
            },
            {
                'name': 'Service 2',
                'id': 2,
                'type': 'Computation',
                'parameters': {'executionTime': '12', 'volumeOfData': '35'},
                'description': 'This is a computation service'
            },
            {
                'name': 'Service 3',
                'id': 3,
                'type': 'Storage',
                'parameters': {'availableMemory': '20'},
                'description': 'This is a storage service'
            },
            {
                'name': 'Service 4',
                'id': 4,
                'type': 'Storage',
                'parameters': { 'availableMemory': '26'},
                'description': 'This is a storage service'
            },
            {
                'name': 'Service 5',
                'id': 5,
                'type': 'Storage',
                'parameters': { 'availableMemory': '30'},
                'description': 'This is a storage service'
            },
            {
                'name': 'Service 6',
                'id': 6,
                'type': 'Storage',
                'parameters': {'availableMemory': '25'},
                'description': 'This is a storage service'
            },
        ]
    }
    
    return [workflow, catalog]

def pretty_print_solution(solution):
        print(json.dumps(solution, indent=4))
    
def main():
    [workflow, catalog] = get_sample_data()
    solution = compare_workflow_and_catalog(workflow, catalog)
    # Pretty print the solution
    pretty_print_solution(solution)
    
main()