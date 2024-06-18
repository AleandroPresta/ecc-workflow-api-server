# Logging and debugging section
from icecream import ic
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

import sys
  
# append the path of the parent directory
sys.path.append('..')

from app.api.lib.utils import find_closest_solution, extract_inequalities, extract_search_space, parse_inequalities, solve_computation_inequalities, \
    extract_reference_points, extract_symbols
    
from app.api.lib.categorizator import categorize_nodes_by_type, categorize_catalog_by_type

'''
    This function finds the closest solution to a given workflow in the catalog. The nodes inside the
    workflow must have all the same 'type'.
    Example of usage:
'''
def find_closest_solution_for_type(type_workflow, type_catalog, distance_function, VERBOSE):
    logging.info("API Called: find_closest_solution_for_type")
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
        logging.debug("Verbose mode is on")
        ic(ineq_sets)
        ic(reference_points)
        ic(inequalities)
        ic(search_space)
        ic(solutions)
        ic(closest_solutions)
    
    return closest_solutions
'''
    Given a workflow and a catalog, this function finds the closest solution to each node in the
    workflow by dividing the nodes by type and calling the find_closest_solution_for_type function.
'''
def process_workflow_catalog(workflow, catalog, distance_function, VERBOSE=False):
    logging.info("API Called: process_workflow_catalog")
    categorized_workflow = categorize_nodes_by_type(workflow)
    categorized_catalog = categorize_catalog_by_type(catalog)
    
    closest_solutions = {}
    for type_workflow, nodes_workflow in categorized_workflow.items():
        closest_solutions[type_workflow] = find_closest_solution_for_type(categorized_workflow[type_workflow], categorized_catalog[type_workflow], distance_function, VERBOSE)
    return closest_solutions