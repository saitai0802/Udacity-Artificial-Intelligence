"""
We will also make two simplifying assumptions in order to adhere to the conventions of Thad's quizzes:
Assumption 1: a state is terminal if the active player has no remaining moves
Assumption 2: the board utility is -1 if it terminates at a max level, and +1 if it terminates at a min level

Sai: Actually, the first assumption is only required in order to allow the second assumption.
"""
def terminal_test(gameState):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    return not bool(gameState.get_legal_moves())  # by Assumption 1


def min_value(gameState):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
        return 1  # by Assumption 2 - 係min尼層無棋行，上一層個max嬴左。
    v = float("inf")
    for m in gameState.get_legal_moves():
        v = min(v, max_value(gameState.forecast_move(m))) # if there is only one -1, that is a bad sub tree
    return v


def max_value(gameState):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
        return -1  # by assumption 2 - 係max尼層無棋行，上一層個min嬴左。
    v = float("-inf")
    for m in gameState.get_legal_moves():
        v = max(v, min_value(gameState.forecast_move(m))) # if there is only one 1, that is a good sub tree
    return v
