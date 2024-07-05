# Problem: Bus Routes - https://leetcode.com/problems/bus-routes/

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph= defaultdict(list)
        for i in range(len(routes)):
            for j in routes[i]:
                graph[j].append(i)
        queue=deque([(source,0)])
        visited=set()
        bsv=set()
        while queue:
            node,c=queue.popleft()
            if node==target:
                return c
            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    for j in routes[i]:
                        if j not in bsv:
                            queue.append((j,c+1))
        return -1

        