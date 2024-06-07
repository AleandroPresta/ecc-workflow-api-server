import json
import math
from sympy.parsing.sympy_parser import parse_expr
from sympy import And, symbols

def pretty_print_solution(solution):
        print(json.dumps(solution, indent=4))
        
# Define a function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two n-dimensional points."""
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

# Define a function to find the point in a set that is closest to a reference point using a distance function
def closest_point(reference_point, points, distance_function=euclidean_distance):
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
                ...
            ]
        }
        output:
        [
            [('executionTime', '<=', 10), ('volumeOfData', '>=', 25)],
            ...
        ]
'''
def extract_inequalities(workflow):
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
    inequalities = []
    # Construct inequalities for each point
    for sets in inequalities_set:
        set = []
        for expression in sets:
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
    search_space = []
    for service in catalog['services']:
        parameters = service['parameters']
        point = tuple(parameters.values())
        search_space.append(point)
    return search_space

'''
    Given an inequalities system and a search space, it solves the inequalities system.
    Given the need to explicitly define the symbols for the variables, this function is not generic,
    it needs to be adapted to the specific variables used in the inequalities (in this case executionTime and volumeOfData).
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
        output:
        [
            [(5, 25), (10, 30), (9, 30)],
            [(12, 25), (11, 26)]
        ]
'''
def solve_computation_inequalities(inequalities, search_space):
    # Define symbols for variables
    executionTime, volumeOfData = symbols('executionTime volumeOfData')
    
    solutions = []
    
    for ineq in inequalities:
        print(f"Solving inequality: {ineq}")
        solutions_set = []
        for point in search_space:
            satisfies_inequalities = ineq.subs({executionTime: point[0], volumeOfData: point[1]})
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
    closest_solutions = []
    # Finds the closest solution to the relative reference point
    for (reference_point, solution) in (zip(reference_points, solutions)):
        closest = closest_point(reference_point, solution, distance_function=distance_function)
        closest_solutions.append(closest)
    return closest_solutions