from inequalities_solver import find_closest_solution_for_type
from inequalities_utils import euclidean_distance

def test2(VERBOSE=False):
    storage_workflow = {
        'nodes': [
            {
                'name': 'Storage 1',
                'id': 1,
                'type': 'Storage',
                'parameters': [
                    {
                        'name': 'availableMemory',
                        'value': 10,
                        'type': '<='
                    },
                    {
                        'name' : 'storageSpeed',
                        'value': 5,
                        'type': '>'
                    },
                    {
                        'name' : 'storageType',
                        'value': 1, # NoSQL
                        'type': '=='
                    }
                ],
            },
            {
                'name': 'Storage 2',
                'id': 2,
                'type': 'Storage',
                'parameters': [
                    {
                        'name': 'availableMemory',
                        'value': 11,
                        'type': '>'
                    },
                    {
                        'name' : 'storageSpeed',
                        'value': 6,
                        'type': '<'
                    },
                    {
                        'name' : 'storageType',
                        'value': 2, # SQL
                        'type': '=='
                    }
                ],
            },
            {
                'name': 'Storage 3',
                'id': 3,
                'type': 'Storage',
                'parameters': [
                    {
                        'name': 'availableMemory',
                        'value': 20,
                        'type': '=='
                    },
                    {
                        'name' : 'storageSpeed',
                        'value': 7,
                        'type': '>'
                    },
                    {
                        'name' : 'storageType',
                        'value': 3, # Graph
                        'type': '=='
                    }
                ],
            }
                
        ]
    }
    
    storage_catalog = {
        'services': [
            {
                'name': 'Service 0',
                'id': 0,
                'type': 'Storage',
                'parameters': {
                    'availableMemory': 5,
                    'storageSpeed': 6,
                    'storageType': 1
                },
            },
            {
                'name': 'Service 1',
                'id': 1,
                'type': 'Storage',
                'parameters': {
                    'availableMemory': 10,
                    'storageSpeed': 5,
                    'storageType': 1
                },
            },
            {
                'name': 'Service 2',
                'id': 2,
                'type': 'Storage',
                'parameters': {
                    'availableMemory': 15,
                    'storageSpeed': 7,
                    'storageType': 2
                },
            },
            {
                'name': 'Service 3',
                'id': 2,
                'type': 'Storage',
                'parameters': {
                    'availableMemory': 15,
                    'storageSpeed': 7,
                    'storageType': 2
                },
            },
            {
                'name': 'Service 4',
                'id': 3,
                'type': 'Storage',
                'parameters': {
                    'availableMemory': 20,
                    'storageSpeed': 8,
                    'storageType': 3
                },
            }
        ]
    }
    
    return find_closest_solution_for_type(storage_workflow, storage_catalog, euclidean_distance, VERBOSE)

def test1(VERBOSE=False):
    computations_workflow = {
        'nodes': [            
            {
                'name': 'Computation 1',
                'id': 1,
                'type': 'Computation',
                'parameters': [
                    {
                        'name' : 'executionTime',
                        'value': 10,
                        'type': '<='
                    },
                    {
                        'name': 'volumeOfData',
                        'value': 25,
                        'type': '>='
                    },    
                ],
            },
            {
                'name': 'Computation 2',
                'id': 2,
                'type': 'Computation',
                'parameters': [
                    {
                        'name': 'executionTime',
                        'value': 11,
                        'type': '<='
                    },
                    {
                        'name': 'volumeOfData',
                        'value': 26,
                        'type': '<='
                    },    
                ],
            },
            {
                'name': 'Computation 3',
                'id': 3,
                'type': 'Computation',
                'parameters': [
                    {
                        'name': 'executionTime',
                        'value': 10,
                        'type': '=='
                    },
                    {
                        'name': 'volumeOfData',
                        'value': 25,
                        'type': '>='
                    },    
                ],
            }
        ]
    }

    computations_catalog = {
        'services': [
            {
                'name': 'Service 0',
                'id': 0,
                'type': 'Computation',
                'parameters': {
                    'executionTime': 5, 
                    'volumeOfData': 25
                },
            },
            {
                'name': 'Service 1',
                'id': 1,
                'type': 'Computation',
                'parameters': {
                    'executionTime': 10, 
                    'volumeOfData': 25
                },
            },
            {
                'name': 'Service 2',
                'id': 2,
                'type': 'Computation',
                'parameters': {
                    'executionTime': 15, 
                    'volumeOfData': 25
                },
            },
            {
                'name': 'Service 3',
                'id': 3,
                'type': 'Computation',
                'parameters': {
                    'executionTime': 5, 
                    'volumeOfData': 30
                },
            }
        ]
    }
    
    return find_closest_solution_for_type(computations_workflow, computations_catalog, euclidean_distance, VERBOSE)
    
def main():
    solution1 = test1()
    print(solution1)
    
    solution2 = test2(VERBOSE=True)
    print(solution2)
    
main()