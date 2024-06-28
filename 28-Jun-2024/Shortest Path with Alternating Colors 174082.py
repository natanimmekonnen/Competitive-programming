# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

from collections import deque
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
   
        graph = [[[], []] for _ in range(n)]
        
        for x, y in redEdges:
            graph[x][0].append(y)
        for i, j in blueEdges:
            graph[i][1].append(j)
        
        queue = deque([(0, 0, 0), (0, 1, 0)]) 
        visited = set([(0, 0), (0, 1)]) 
        val = [-1] * n  
        
        while queue:
            node, color, length = queue.popleft()
            
            if val[node] == -1:
                val[node] = length
            else:
                val[node] = min(val[node], length)
        
            alt = 1 - color
            for neighbor in graph[node][alt]:
                if (neighbor, alt) not in visited:
                    visited.add((neighbor, alt))
                    queue.append((neighbor, alt, length + 1))
        
        return val

