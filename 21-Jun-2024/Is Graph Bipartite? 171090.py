# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color=[-1 for i in range(n)]
        def bipart(s):
            color[s]=0
            stack=[s]
            while stack:
                v=stack.pop()
                for i in graph[v]:
                    if color[v]==color[i]:
                        return False
                    if color[i]==-1:
                        stack.append(i)
                        color[i]=1-color[v]
            return True
        for i in range(n):
            if color[i]==-1 and not bipart(i):
                return False
        return True
