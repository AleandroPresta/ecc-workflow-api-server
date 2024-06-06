import json
import math

def pretty_print_solution(solution):
        print(json.dumps(solution, indent=4))
        
# Define a function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two n-dimensional points."""
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

# Define a function to find the point in a set that is closest to a reference point
def closest_point(reference_point, points):
    """Find the point in the set that is closest to the reference point."""
    closest = None
    min_distance = float('inf')
    for point in points:
        distance = euclidean_distance(reference_point, point)
        if distance < min_distance:
            min_distance = distance
            closest = point
    return closest

'''
    The function extract_inequalities to extract inequalities from a workflow.
'''
def extract_inequalities(workflow):
    """Extract the list of points from the workflow."""
    points = []
    for node in workflow['nodes']:
        ineq = []
        parameters = node.get('parameters', [])
        for parameter in parameters:
            ineq.append((parameter['name'], parameter['type'], int(parameter['value'])))
        points.append(ineq)
    return points

def extract_search_space(catalog):
    """Extract the search space points from the catalog."""
    search_space = []
    for service in catalog['services']:
        parameters = service['parameters']
        point = tuple(parameters.values())
        search_space.append(point)
    return search_space