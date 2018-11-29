import sys, os
#sys.path.insert(0, os.path.realpath('./'))
sys.path.append(os.path.abspath('./'))
from utils import *

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    #pass
    values = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)
    assert len(values) == 81, "Input grid must be a string of length 81 (9x9)"
    # boxes = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B1', 'B2',....]
    # grid = ..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..
    return dict(zip(boxes, values))
    # Return {'A1': '123456789', 'A2': '123456789', 'A3': '3', 'A4': '123456789',....}

# Step 1:
# display(grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    #syntactic sugar
    #https://stackoverflow.com/questions/6475314/python-for-in-loop-preceded-by-a-variable
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    # solved_values = ['A3', 'A5', 'A7', 'B1', 'B4', 'B6', 'B9', 'C3',....]
    for box in solved_values:
        digit = values[box]
        # peer 係本身utils 到set 左
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values

#Step 2:
eliminate(grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))
