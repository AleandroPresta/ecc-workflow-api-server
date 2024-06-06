from sympy import symbols, And, solveset
from utils import closest_point, extract_inequalities, extract_search_space
from sympy.parsing.sympy_parser import parse_expr


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
    ]
}

# Define symbols for variables
executionTime, volumeOfData = symbols('executionTime volumeOfData')

# Extract the points from the workflow
ineq_sets = extract_inequalities(workflow)

# Define a list to hold the inequalities
inequalities = []

# Construct inequalities for each point
for sets in ineq_sets:
    set = []
    for expression in sets:
        e = f'{expression[0]} {expression[1]} {expression[2]}'
        parsed_e = parse_expr(e)
        set.append(parsed_e)
    inequalities.append(And(*set))
    
print("Inequalities:", inequalities)    

'''# Combine all inequalities with 'And'
combined_inequalities = []
for ineq in inequalities:
    print(ineq)
    combined_inequalities.append(And(*ineq))
print("Combined inequalities:", combined_inequalities)

# Define a list of points (example)
# Extract the search space from the catalog
search_space = extract_search_space(catalog)
print("Search space:" , search_space)

# Define a list to hold the solutions
solutions = []

# Check each point against the inequalities
for point in search_space:
    satisfies_inequalities = all(ineq.subs({executionTime: point[0], volumeOfData: point[1]}) for ineq in inequalities)
    if satisfies_inequalities:
        solutions.append(point)

print("Solutions:", solutions) '''