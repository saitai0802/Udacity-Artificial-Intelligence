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
    assert len(grid) == 81, "Input grid must be a string of length 81 (9x9)"
    # boxes = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B1', 'B2',....]
    # grid = ..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..
    return dict(zip(boxes, grid))
    # Return {'A1': '.', 'A2': '.', 'A3': '3',... }

# Sai - testing
display(grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))
