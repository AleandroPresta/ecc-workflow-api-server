from workflow_catalog_evaluator import compare_workflow_and_catalog
import json

def get_sample_data():
    workflow = {
        'nodes': [
            {
                'name': 'Device',
                'id': 0,
                'type': 'Device',
                'description': 'This is a device',
                'x': 26,
                'y': 27,
                'width': 350,
                'inputConnectors': [{'name': 'in_0_0'}],
                'outputConnectors': [{'name': 'out_0_0'}]
            },
            {
                'name': 'Computation',
                'id': 1,
                'type': 'Computation',
                'parameters': {'executionTime': 10, 'volumeOfData': 25},
                'description': 'This is a computation',
                'x': 418,
                'y': 138,
                'inputConnectors': [{'name': 'in_1_0'}],
                'outputConnectors': [{'name': 'out_1_0'}],
                'width': 250
            },
            {
                'name': 'Storage',
                'id': 2,
                'type': 'Storage',
                'parameters': {'availableMemory': 25},
                'description': 'This is a storage',
                'x': 687,
                'y': 296,
                'inputConnectors': [{'name': 'in_2_0'}],
                'outputConnectors': [{'name': 'out_2_0'}],
                'width': 250
            },
            {
                'name': 'Communication',
                'id': 3,
                'type': 'Communication',
                'parameters': {},
                'description': 'This is a communication',
                'x': 985,
                'y': 423,
                'inputConnectors': [{'name': 'in_3_0'}],
                'outputConnectors': [{'name': 'out_3_0'}],
                'width': 250
            }
        ],
        'connections': [
            {
                'name': 'Connection 1',
                'source': {'nodeID': 0, 'connectorIndex': 0},
                'dest': {'nodeID': 1, 'connectorIndex': 0}
            },
            {
                'name': 'Connection 2',
                'source': {'nodeID': 1, 'connectorIndex': 0},
                'dest': {'nodeID': 2, 'connectorIndex': 0}
            },
            {
                'name': 'Connection 3',
                'source': {'nodeID': 2, 'connectorIndex': 0},
                'dest': {'nodeID': 3, 'connectorIndex': 0}
            }
        ]
    }

    catalog = {
        'services': [
            {
                'name': 'Service 1',
                'id': 0,
                'type': 'Computation',
                'parameters': {'executionTime': '5', 'volumeOfData': '25'},
                'description': 'This is a computation service'
            },
            {
                'name': 'Service 2',
                'id': 1,
                'type': 'Computation',
                'parameters': {'executionTime': '11', 'volumeOfData': '25'},
                'description': 'This is a computation service'
            },
            {
                'name': 'Service 3',
                'id': 2,
                'type': 'Storage',
                'parameters': {'availableMemory': '20'},
                'description': 'This is a storage service'
            },
            {
                'name': 'Service 4',
                'id': 3,
                'type': 'Storage',
                'parameters': { 'availableMemory': '30'},
                'description': 'This is a storage service'
            },
            {
                'name': 'Service 5',
                'id': 4,
                'type': 'Communication',
                'parameters': {},
                'description': 'This is a communication service'
            }
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