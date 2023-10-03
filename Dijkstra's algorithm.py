import heapq

def shortest_path(graph, source, destination):
    # Initialize distances and predecessors
    distances = {node: float('infinity') for node in graph}
    predecessors = {node: None for node in graph}
    distances[source] = 0
    
    # Initialize priority queue with source node
    priority_queue = [(0, source)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node == destination:
            path = []
            while predecessors[current_node] is not None:
                path.insert(0, current_node)
                current_node = predecessors[current_node]
            path.insert(0, source)
            return path, distances[destination]
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return None, float('infinity')
