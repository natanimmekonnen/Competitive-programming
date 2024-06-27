# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import deque, defaultdict

def build_graph(edges):
    graph = defaultdict(list)
    for _ in range(edges):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph

def bfs_shortest_path(graph, source, target):
    prev = {source: -1}
    queue = deque([source])
    
    while queue:
        node = queue.popleft()
        if node == target:
            break
        for neighbour in graph[node]:
            if neighbour not in prev:
                prev[neighbour] = node
                queue.append(neighbour)
    
    return prev

def reconstruct_path(prev, target):
    if target not in prev:
        return -1, []
    
    path = []
    current = target
    while current != -1:
        path.append(current)
        current = prev[current]
    
    return len(path) - 1, path[::-1]

def shortestPath():
    nodes, edges = map(int, input().split())
    source, target = map(int, input().split())
    
    graph = build_graph(edges)
    prev = bfs_shortest_path(graph, source, target)
    distance, path = reconstruct_path(prev, target)
    
    print(distance)
    if distance != -1:
        print(path)

shortestPath()

