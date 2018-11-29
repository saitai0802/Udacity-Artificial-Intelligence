import sys, os
#sys.path.insert(0, os.path.realpath('./'))
sys.path.append(os.path.abspath('./'))
from utils import *

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        values = eliminate(values)

        # Your code here: Use the Only Choice Strategy
        values = only_choice(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop. (Sai: important!)
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values: (Sai: important!)
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

print(
reduce_puzzle(grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))
);
