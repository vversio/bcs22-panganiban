import heapq

location = ["Home", "Store A", "Store B", "School", "Intersection"]

path_list = [

    [(1, 7), (2, 14), (4, 25)],

    [(0, 7), (2, 5)],

    [(3, 7)],

    [(2, 7), (4, 7)],

    [(3, 7)],

]

# Define the graph and distances

graph = path_list

distances = [float('inf')] * len(location)

distances[0] = 0  # Starting node is Home (index 0)

# Priority queue to keep track of nodes to visit

priority_queue = [(0, 0)]

# Keep track of the previous node for each location

previous_nodes = [None] * len(location)

while priority_queue:

    dist, current_node = heapq.heappop(priority_queue)

    if dist > distances[current_node]:
        continue

    for neighbor, edge_distance in graph[current_node]:

        total_distance = dist + edge_distance

        if total_distance < distances[neighbor]:
            distances[neighbor] = total_distance

            previous_nodes[neighbor] = current_node

            heapq.heappush(priority_queue, (total_distance, neighbor))

# Shortest distance from Home to School (index 3)

shortest_distance = distances[3]

print(f"The shortest distance from Home to School is: {shortest_distance}")

# Construct the path from Home to School

path = []

current_location = 3  # School (index 3)

while current_location is not None:
    path.insert(0, current_location)

    current_location = previous_nodes[current_location]

print("The path from Home to School is:", [location[node] for node in path])
