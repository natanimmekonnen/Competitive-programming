# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        out_degree = [0] * n

        for node in range(n):
            for neighbor in graph[node]:
                reverse_graph[neighbor].append(node)
            out_degree[node] = len(graph[node])

        queue = [i for i in range(n) if out_degree[i] == 0]
        safe = [False] * n

        while queue:
            node = queue.pop()
            safe[node] = True
            for neighbor in reverse_graph[node]:
                out_degree[neighbor] -= 1
                if out_degree[neighbor] == 0:
                    queue.append(neighbor)

        result = [i for i in range(n) if safe[i]]
        result.sort()
        return result

        