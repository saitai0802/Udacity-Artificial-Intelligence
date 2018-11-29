from utils import *

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)

    # Sai: this line is to make sure at least solved once
    if values is False:
        return False ## Failed earlier

    # boxes = 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B1', 'B2', ....';
    # all: Return True if all elements of the iterable are true
    if all(len(values[s]) == 1 for s in boxes):
        return values ## Solved!

    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)

    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        #如果用左reduce_puzzle 都搞唔到，就要行尼個recursive search 去估哂所有posibilities
        attempt = search(new_sudoku)
        if attempt:
            return attempt

# easy_sudoku = 唔使search 都已經做好哂
easy_sudoku = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
hard_sudoku = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
display(search( reduce_puzzle(grid_values(hard_sudoku)) ));
