import json
import math
from sympy.parsing.sympy_parser import parse_expr
from sympy import And, symbols
from icecream import ic

import logging

def pretty_print_solution(solution):
        print(json.dumps(solution, indent=4))
        
# Define a function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two n-dimensional points."""
    logging.debug(f'Calculating Euclidean distance between {point1} and {point2}')
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

# Define a function to find the point in a set that is closest to a reference point using a distance function
def closest_point(reference_point, points, distance_function=euclidean_distance):
    logging.debug(f'Finding the closest point to {reference_point} in {points}')
    closest = None
    min_distance = float('inf')
    for point in points:
        distance = distance_function(reference_point, point)
        if distance < min_distance:
            min_distance = distance
            closest = point
    return closest

'''
    Given a workflow, it extracts the inequalities from the parameters of each node.
    Example of usage:
        input:
        workflow = {
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
                            'name' : 'executionTime',
                            'value': 11,
                            'type': '<='
                        },
                        {
                            'name': 'volumeOfData',
                            'value': 26,
                            'type': '<='
                        },    
                    ],
                }
                ...
            ]
        }
        output:
        [
            [('executionTime', '<=', 10), ('volumeOfData', '>=', 25)], 
            [('executionTime', '<=', 11), ('volumeOfData', '<=', 26)],
            ...
        ]
'''
def extract_inequalities(workflow):
    logging.debug(f'Extracting inequalities from workflow: {workflow}')
    points = []
    for node in workflow['nodes']:
        ineq = []
        parameters = node.get('parameters', [])
        for parameter in parameters:
            ineq.append((parameter['name'], parameter['type'], int(parameter['value'])))
        points.append(ineq)
    return points

'''
    Given a workflow, it extracts the reference points from the parameters of each node.
    Example of usage:
        input:
        workflow = {
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
                ...
            ]
        }
        output:
        [
            [10, 25],
            ...
        ]
'''
def extract_reference_points(workflow):
    logging.debug(f'Extracting reference points from workflow: {workflow}')
    points = []
    for node in workflow['nodes']:
        p = []
        parameters = node.get('parameters', [])
        for parameter in parameters:
            p.append(int(parameter['value']))
        points.append(p)
    return points

'''
    Given a set of inequalities, it parses them into a format that can be used by the solver.
    Example of usage:
        input:
        [
            [('executionTime', '<=', 10), ('volumeOfData', '>=', 25)],
            ...
        ]
        output:
        [
            And(executionTime <= 10, volumeOfData >= 25),
            ...
        ]
'''
def parse_inequalities(inequalities_set):
    logging.debug(f'Parsing inequalities: {inequalities_set}')
    inequalities = []
    # Construct inequalities for each point
    for sets in inequalities_set:
        set = []
        for expression in sets:
            if(expression[1] == '=='):
                e = f'Eq({expression[0]},{expression[2]})'
            else:
                e = f'{expression[0]} {expression[1]} {expression[2]}'
            parsed_e = parse_expr(e)
            set.append(parsed_e)
        inequalities.append(And(*set))
    return inequalities

'''
    Given a catalog, extracts the search space from the parameters of each service.
    Example of usage:
        input:
        catalog = {
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
                ...
            ]
        }
        output:
        [
            (5, 25),
            ...
        ]
'''
def extract_search_space(catalog):
    logging.debug(f'Extracting search space from catalog: {catalog}')
    search_space = []
    for service in catalog['services']:
        parameters = service['parameters']
        point = tuple(parameters.values())
        search_space.append(point)
    return search_space

'''
    Extract the symbols for the inequalities. It is necessary to have symbols in order to solve the inequalities with the library sympy.
    Example of usage:
        input:
        workflow = {
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
                ...
            ]
        }
        output:
        ['executionTime', 'volumeOfData']
        
        NOTE: it extracts the symbols from the first node. If the symbols are different in other nodes, it will not work.
'''
def extract_symbols(workflow):
    logging.debug(f'Extracting symbols from workflow: {workflow}')
    ineq_symbols = []
    # Takes a reference node and extracts the symbols from the parameters
    reference_node = workflow['nodes'][0]
    parameters = reference_node.get('parameters', [])
    for parameter in parameters:
        ineq_symbols.append(parameter['name'])
    return ineq_symbols

'''
    Given an inequalities system and a search space and a set of symbols (in string format) for the inequalities, it solves the inequalities system.
    Example of usage:
        input:
        inequalities = [
            And(executionTime <= 10, volumeOfData >= 25),
            And(executionTime <= 11, volumeOfData <= 26)
        ]
        search_space = [
            (5, 25), 
            (12, 25), 
            (10, 30), 
            (11, 26), 
            (9, 30)
        ]
        symbols_string = 'executionTime volumeOfData'
        output:
        [
            [(5, 25), (10, 30), (9, 30)],
            [(12, 25), (11, 26)]
        ]
'''
def solve_computation_inequalities(inequalities, search_space, symbols_string):
    logging.debug(f'Solving inequalities: {inequalities} with search space: {search_space} and symbols: {symbols_string}')
    # Define symbols for variables
    ineq_symbles = symbols(symbols_string)
    
    solutions = []
    
    for ineq in inequalities:
        solutions_set = []
        for point in search_space:
            if (len(point) != len(ineq_symbles)):
                raise ValueError(f'The number of variables in \n{point} \ndoes not match the number of variables in \n {inequalities}\n')
            
            satisfies_inequalities = ineq.subs(
                {symbol: value for symbol, value in zip(ineq_symbles, point)}
            )
            if satisfies_inequalities:
                solutions_set.append(point)
        solutions.append(solutions_set)
    return solutions

'''
    Given a set of reference points and a set of solutions, it finds the closest solution to each reference point using a distance function.
    Example of usage:
        input:
        reference_points = [
            [10, 25],
            [11, 26]
        ]
        solutions = [
            [(5, 25), (10, 30), (9, 30)],
            [(12, 25), (11, 26)]
        ]
        distance_function = euclidean_distance
        output:
        [
            (10, 30),
            (11, 26)
        ]
'''
def find_closest_solution(reference_points, solutions, distance_function):
    logging.debug(f'Finding the closest solution to reference points: {reference_points} in solutions: {solutions}')
    closest_solutions = []
    # Finds the closest solution to the relative reference point
    for (reference_point, solution) in (zip(reference_points, solutions)):
        closest = closest_point(reference_point, solution, distance_function=distance_function)
        closest_solutions.append(closest)
    return closest_solutions