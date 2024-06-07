from inequalities_solver import find_closest_solution_for_type
from inequalities_utils import euclidean_distance

def test2():
    return None 

def test1():
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
                    'executionTime': 12, 
                    'volumeOfData': 25
                },
            },
            {
                'name': 'Service 2',
                'id': 2,
                'type': 'Computation',
                'parameters': {
                    'executionTime': 10, 
                    'volumeOfData': 30
                },
            },
            {
                'name': 'Service 3',
                'id': 3,
                'type': 'Computation',
                'parameters': {
                    'executionTime': 11, 
                    'volumeOfData': 26
                },
            },
            {
                'name': 'Service 4',
                'id': 4,
                'type': 'Computation',
                'parameters': {
                    'executionTime': 9, 
                    'volumeOfData': 30
                },
            }
        ]
    }
    
    return find_closest_solution_for_type(computations_workflow, computations_catalog, euclidean_distance, VERBOSE=True)
    
def main():
    solution1 = test1()
    print(solution1)
    
main()