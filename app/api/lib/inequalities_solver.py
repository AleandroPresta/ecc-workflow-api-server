from .inequalities_utils import find_closest_solution, extract_inequalities, extract_search_space, parse_inequalities, solve_computation_inequalities, \
    extract_reference_points, extract_symbols

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
        print(f'ineq_sets: {ineq_sets}\n')
        print(f'Reference points: {reference_points}\n')
        print(f"Inequalities: {inequalities}\n")
        print(f"Search space: {search_space}\n")
        print(f"Solutions: {solutions}\n")
        print(f"Closest solutions: {closest_solutions}\n")
    
    return closest_solutions

