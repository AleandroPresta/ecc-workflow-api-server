import sys
sys.path.append('app/api')

from lib.inequalities_utils import categorize_nodes_by_type, pretty_print_solution

def test1():
    workflow = {
        'nodes': [
            {
                'name': 'Storage 1',
                'id': 1,
                'type': 'Storage',
            },
            {
                'name': 'Storage 2',
                'id': 2,
                'type': 'Storage',
            },
            {
                'name': 'Computation 1',
                'id': 3,
                'type': 'Computation',
            },
            {
                'name': 'Computation 2',
                'id': 4,
                'type': 'Computation',
            },
            {
                'name': 'Storage 3',
                'id': 5,
                'type': 'Storage',
            },
            {
                'name': 'Communication 1',
                'id': 6,
                'type': 'Communication',
            }
        ]
    }

    solution = categorize_nodes_by_type(workflow)
    return solution
    
def main():
    solution1 = test1()
    pretty_print_solution(solution1)
    
main()