# Problem: Detect Cycle in an Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

    def isCycle(self, V: int, adj: List[List[int]]) -> bool:   

        def dfs(v, parent):
            visited[v] = True
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    if dfs(neighbor, v):
                        return True
                elif neighbor != parent:  # Back edge found, cycle exists
                    return True
            return False

        visited = [False] * V

        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return True
        return False
