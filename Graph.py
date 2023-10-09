from collections import defaultdict

# Function for adding edge to graph
graph = defaultdict(list)

def addEdge(graph, u, v, cost):
    graph[u].append((v, cost,))

# Definition of function
def generate_edges(graph):
    edges = []

    # For each node in the graph
    for node in graph:
        # For each neighbor node of a single node
        for neighbor, cost in graph[node]:
            # If edge exists, then append
            edges.append((node, neighbor, cost))
    return edges

# Declaration of graph as a dictionary
addEdge(graph, 'S', 'A', 3)
addEdge(graph, 'S', 'B', 1)
addEdge(graph, 'A', 'B', 2)
addEdge(graph, 'A', 'C', 2)
addEdge(graph, 'B', 'C', 3)
addEdge(graph, 'C', 'D', 4)
addEdge(graph, 'C', 'G', 4)
addEdge(graph, 'D', 'G', 1)

# Driver function call to print the generated graph
edges = generate_edges(graph)
for edge in edges:
    u, v, cost= edge
    print(f'Edge: ({u} -> {v}), Cost: {cost}')


    graph = {
    'S': {'neighbors': [('A', 3), ('B', 1)], 'heuristic': 7},
    'A': {'neighbors': [('B', 2), ('C', 2)], 'heuristic': 5},
    'B': {'neighbors': [('C', 3)], 'heuristic': 7},
    'C': {'neighbors': [('D', 4), ('G', 4)], 'heuristic': 4},
    'D': {'neighbors': [('G', 1)], 'heuristic': 1},
    'G': {'neighbors': [], 'heuristic': 0}
}

for node, data in graph.items():
    neighbors = data['neighbors']
    heuristic = data['heuristic']
    print(f"Node '{node}' - Heuristic: {heuristic}")
    print(f"Neighbors: {', '.join([f'{neighbor} ({weight})' for neighbor, weight in neighbors])}\n")

