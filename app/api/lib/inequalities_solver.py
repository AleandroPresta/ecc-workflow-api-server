from inequalities_utils import find_closest_solution, extract_inequalities, extract_search_space, parse_inequalities, solve_computation_inequalities, \
    extract_reference_points, euclidean_distance, extract_symbols

def find_closest_solution_for_type(type_workflow, type_catalog, distance_function, VERBOSE):
    # Extract the points from the workflow
    ineq_sets = extract_inequalities(type_workflow)

    # Extract the reference points
    reference_points = extract_reference_points(type_workflow)

    # Define a list to hold the inequalities
    inequalities = parse_inequalities(ineq_sets)

    # Extract the search space from the catalog
    search_space = extract_search_space(type_catalog)
    
    # Define a list to hold the solutions
    symbols_string = extract_symbols(type_workflow)
    solutions = solve_computation_inequalities(inequalities, search_space, symbols_string)

    closest_solutions = find_closest_solution(reference_points, solutions, distance_function)
    
    if(VERBOSE):
        print(f'ineq_sets: {ineq_sets}')
        print(f'Reference points: {reference_points}')
        print("Inequalities:", inequalities)
        print("Search space:" , search_space)
        print("Solutions:", solutions)
        print("Closest solutions:", closest_solutions)
    
    return closest_solutions

'''def find_closest_solution(workflow, catalog, distance_function):
    # Create one workflow for each type
    types_workflow = set([node['type'] for node in workflow['nodes']])
    # Create one catalog for each type
    types_catalog = set([service['type'] for service in catalog['services']])
    
    solutions = []
    for type_workflow, type_catalog in zip(types_workflow, types_catalog):
        solutions.append(find_closest_solution_for_type(type_workflow, type_catalog, distance_function))
'''