# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        visited=set()
        def dfs(s):
            if s==destination:
                return True
            visited.add(s)
            for i in graph[s]:
                if i not in visited:
                   if dfs(i):
                    return True
            return False
        return dfs(source)
    