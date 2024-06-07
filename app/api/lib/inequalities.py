from utils import find_closest_solution, extract_inequalities, extract_search_space, parse_inequalities, solve_computation_inequalities, \
    extract_reference_points, euclidean_distance, extract_symbols

def find_closest_solution_for_type(type_workflow, type_catalog, distance_function):
    # Extract the points from the workflow
    ineq_sets = extract_inequalities(type_workflow)

    # Extract the reference points
    reference_points = extract_reference_points(type_workflow)
    print(f'Reference points: {reference_points}')

    # Define a list to hold the inequalities
    inequalities = parse_inequalities(ineq_sets)
    print("Inequalities:", inequalities)

    # Define a list of points (example)
    # Extract the search space from the catalog
    search_space = extract_search_space(type_catalog)
    print("Search space:" , search_space)

    # Define a list to hold the solutions
    symbols_string = extract_symbols(type_workflow)
    solutions = solve_computation_inequalities(inequalities, search_space, symbols_string)
    print("Solutions:", solutions)

    closest_solutions = find_closest_solution(reference_points, solutions, distance_function)
    print("Closest solutions:", closest_solutions)
    
    return closest_solutions

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
    
    find_closest_solution_for_type(computations_workflow, computations_catalog, euclidean_distance)
    
def main():
    test1()
    
main()