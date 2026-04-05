graph = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0],
]

def tsp_nearest_neighbor(graph):
    n = len(graph)
    visited = [False] * n

    path = []
    total_cost = 0

    current_city = 0 
    visited[current_city] = True
    path.append(current_city)

    for _ in range(n-1):
        nearest_city = None
        min_distance = float('inf')

        # find the nearest unvisited city
        for city in range(n):
            if not visited[city] and graph[current_city][city] < min_distance:
                min_distance = graph[current_city][city]
                nearest_city = city

        # move to that city
        path.append(nearest_city)
        visited[nearest_city] = True
        total_cost += min_distance
        current_city = nearest_city

    # return to start
    total_cost += graph[current_city][path[0]]
    path.append(path[0])

    return path, total_cost

path, cost = tsp_nearest_neighbor(graph)

print('Path :', path)
print('Total cost :', cost)
