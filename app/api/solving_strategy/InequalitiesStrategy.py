from SolvingStrategy import SolvingStrategy
import logging
import Categorizator
import utils
from icecream import ic

class InequalitiesStrategy(SolvingStrategy):
    
    def __init__(self, distance_function, VERBOSE: bool):
        self.distance_function = distance_function
        self.VERBOSE = VERBOSE
    
    def solve(self, workflow, catalog) -> None:
        logging.info("API Called: process_workflow_catalog")
        categorized_workflow = Categorizator.categorize_nodes_by_type(workflow)
        categorized_catalog = Categorizator.categorize_catalog_by_type(catalog)
        
        closest_solutions = {}
        for type_workflow, nodes_workflow in categorized_workflow.items():
            closest_solutions[type_workflow] = self.find_closest_solution_for_type(categorized_workflow[type_workflow], categorized_catalog[type_workflow], self.distance_function, self.VERBOSE)
        return closest_solutions
    
    
    '''
        This function finds the closest solution to a given workflow in the catalog. The nodes inside the
        workflow must have all the same 'type'.
        Example of usage:
    '''
    def find_closest_solution_for_type(self, type_workflow: dict, type_catalog: dict, distance_function, VERBOSE: bool) -> dict:
        logging.info("API Called: find_closest_solution_for_type")
        # Extract the points from the workflow
        ineq_sets = utils.extract_inequalities(type_workflow)

        # Extract the reference points
        reference_points = utils.extract_reference_points(type_workflow)

        # Define a list to hold the inequalities
        inequalities = utils.parse_inequalities(ineq_sets)

        # Extract the search space from the catalog
        search_space = utils.extract_search_space(type_catalog)
        
        # Define a list to hold the solutions
        symbols_string = utils.extract_symbols(type_workflow)
        solutions = utils.solve_computation_inequalities(inequalities, search_space, symbols_string)

        closest_solutions = utils.find_closest_solution(reference_points, solutions, distance_function)
        
        if(VERBOSE):
            ic(ineq_sets)
            ic(reference_points)
            ic(inequalities)
            ic(search_space)
            ic(solutions)
            ic(closest_solutions)
        
        return closest_solutions