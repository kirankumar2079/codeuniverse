print("Water Jug problem using DFS")

jug1_capacity = 4
jug2_capacity = 3

initial_state = (0,0)
goal = (0,1)

visited = set()

def is_valid(state):
    x,y = state
    return 0 <= x <= jug1_capacity and 0 <= y <= jug2_capacity

def next_states(state):
    x,y = state
    states = []

    # fill x
    states.append((jug1_capacity,y))
    # fill y
    states.append((x,jug2_capacity))
    # empty x
    states.append((0,y))
    # empty y
    states.append((x,0))
    # x -> y
    pour = min( x , jug2_capacity - y )
    states.append((x-pour , y+pour))
    # y -> x
    pour = min(y , jug1_capacity - x)
    states.append((x+pour , y-pour))

    return states

def dfs(state,path):
    if state in visited:
        return False
    
    visited.add(state)
    path.append(state)
    
    if goal == state:
        print("Solution found")
        for step in path:
            print(step)
        return True
    
    for neighbor in next_states(state):
        if is_valid(neighbor):
            if dfs(neighbor,path.copy()):
                return True
            
    return False


if not dfs(initial_state, []):
    print("No Solution")
