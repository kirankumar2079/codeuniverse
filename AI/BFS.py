from collections import deque

initial_state = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-' 
]

visited = set()


def print_board(state):
    for i in range(0,9,3):
        print(state[i:i+3])
    print()

def check_winner(state):
    winning_pos = [
        # Horizontal
        [0,1,2] , [3,4,5] , [6,7,8],
        # Vertical
        [0,3,6] , [1,4,7] , [2,5,8],
        # diagonal
        [0,4,8] , [2,4,6]
        ]
    
    for pos in winning_pos:
        if state[pos[0]] == state[pos[1]] == state[pos[2]] != '-':
            return state[pos[0]]
    
    return None

def bfs(max_depth=10):
    queue = deque([(initial_state , 'X' , 0)])

    while queue:
        state , player , depth = queue.popleft()
        state_tuple= tuple(state)

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        # print("Depth : " , depth , " | Player : " , player )
        # print_board(state)

        winner = check_winner(state)

        if winner:
            print("Winner : " , winner)
            print("Depth : " , depth , " | Player : " , player )
            print_board(state)
            continue

        if depth >= max_depth:
            continue

        for i in range(9):
            if state[i] == '-':
                new_state = state.copy()
                new_state[i] = player

                next_player = 'O' if player == 'X' else 'X'

                queue.append((new_state, next_player , depth+1))



bfs()