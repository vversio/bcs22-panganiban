import heapq

path_list = [
    ("Home", "Store A", 7),
    ("Home", "Store B", 14),
    ("Home", "Intersection", 25),
    ("Store A", "Home", 7),
    ("Store A", "Store B", 5),
    ("Store B", "School", 7),
    ("School", "Intersection", 7),
    ("Intersection", "School", 7)
]

def shortest_path(path_list, start, end):
    distances = {point: float('inf') for point in set([item[0] for item in path_list] + [item[1] for item in path_list])}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_vertices = {point: None for point in set([item[0] for item in path_list] + [item[1] for item in path_list])}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue

        for pointA, pointB, weight in path_list:
            if pointA == current_vertex:
                distance = current_distance + weight
                if distance < distances[pointB]:
                    distances[pointB] = distance
                    heapq.heappush(priority_queue, (distance, pointB))
                    previous_vertices[pointB] = current_vertex

    shortest_path = []
    while end:
        shortest_path.insert(0, end)
        end = previous_vertices[end]

    return distances, shortest_path

point_a = "Home"
point_b = "School"
shortest_distances, shortest_path = shortest_path(path_list, point_a, point_b)

print("Shortest Distance:", shortest_distances[point_b])
print("Shortest Path:", shortest_path)
