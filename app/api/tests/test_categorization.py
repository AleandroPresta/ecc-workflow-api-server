import sys
import os

# Add the parent directory of 'lib' to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib import utils
from lib import categorizator

import logging

logging_level = logging.DEBUG

# Set up logging
logging.basicConfig(
    level=logging_level,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Check if the logging level is set to DEBUG
if (logging_level == logging.DEBUG):
    VERBOSE = True
else:
    VERBOSE = False


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
    
    solution = categorizator.categorize_catalog_by_type(catalog)
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

    solution = categorizator.categorize_nodes_by_type(workflow)
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
    categorized_workflow = categorizator.categorize_nodes_by_type(workflow)
    categorized_catalog = categorizator.categorize_catalog_by_type(catalog)
    
    return [categorized_workflow, categorized_catalog]
    
def main():
    solution1 = test_workflow()
    # pretty_print_solution(solution1)
    
    solution2 = test_catalog()
    # pretty_print_solution(solution2)
    
    solution3 = test_both()
    utils.pretty_print_solution(solution3)
    
if __name__ == '__main__':
    main()