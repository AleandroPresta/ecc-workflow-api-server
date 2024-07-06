import sys
import os
'''
    This test are used only to check that everything works without errors.
    The result itself of the solving strategy is not tested.
'''

# Add the parent directory to sys.path to be able to import Categorizator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from InequalitiesStrategy import InequalitiesStrategy
import utils

def test_solve1():
    distance_function = utils.euclidean_distance
    VERBOSE: bool = True
    strategy: InequalitiesStrategy = InequalitiesStrategy(distance_function=distance_function, VERBOSE=VERBOSE)
    workflow = {
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
                'name': 'Computation 1',
                'id': 3,
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
                'id': 4,
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
                'id': 5,
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
    
    catalog = {
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
            },
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
    
    strategy.solve(workflow=workflow, catalog=catalog)


def test_solve2():
    distance_function = utils.euclidean_distance
    VERBOSE: bool = True
    strategy: InequalitiesStrategy = InequalitiesStrategy(distance_function=distance_function, VERBOSE=VERBOSE)
    
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
    
    strategy.solve(workflow=storage_workflow, catalog=storage_catalog)


def test_solve3():
    distance_function = utils.euclidean_distance
    VERBOSE: bool = True
    strategy: InequalitiesStrategy = InequalitiesStrategy(distance_function=distance_function, VERBOSE=VERBOSE)
    
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
    
    strategy.solve(workflow=computations_workflow, catalog=computations_catalog)
    

def main() -> None:
    test_solve1()
    print("InequalitiesStrategy tests 1 passed")
    
    test_solve2()
    print("InequalitiesStrategy tests 2 passed")
    
    test_solve3()
    print("InequalitiesStrategy tests 3 passed")

if __name__ == "__main__":
    main()