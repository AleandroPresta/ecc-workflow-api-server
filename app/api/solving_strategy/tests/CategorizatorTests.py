import sys
import os

# Add the parent directory to sys.path to be able to import Categorizator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import Categorizator


def test_catalog():
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
    
    solution = Categorizator.categorize_catalog_by_type(catalog)
    return solution

def test_workflow():
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

    solution = Categorizator.categorize_nodes_by_type(workflow)
    return solution
    
def test_both():
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
    categorized_workflow = Categorizator.categorize_nodes_by_type(workflow)
    categorized_catalog = Categorizator.categorize_catalog_by_type(catalog)
    
    return [categorized_workflow, categorized_catalog]


def main() -> None:
    print(test_catalog())
    print('\n\n')
    print(test_workflow())
    print('\n\n')
    print(test_both())


if __name__ == "__main__":
    main()