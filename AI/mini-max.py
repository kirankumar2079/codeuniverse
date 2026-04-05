game_tree = [
    [3,5],
    [6,9]
]

depth = 2

def minimax(depth, node, maximizing_player):
    if depth == 0:
        return node 
    if maximizing_player:
        best = -float('inf')

        for child in node:
            val = minimax(depth-1 , child , False)
            best = max(best, val)

    else:
        best = float('inf')

        for child in node:
            val = minimax(depth-1 , child , True)
            best = min(best, val)

    return best

optimal_value = minimax(depth, game_tree, True)
print('Optimal Value : ' , optimal_value)