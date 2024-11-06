# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
       
        graph = {i: [] for i in range(1, n + 1)}
        for src, dst, time in times:
            graph[src].append((dst, time))

        pq = [(0, k)]  
        visited = set()
        delays = 0

        while pq:
            time, node = heapq.heappop(pq)

            if node in visited:
                continue

            visited.add(node)
            delays = max(delays, time)

            for neighbor, neighbor_time in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (time + neighbor_time, neighbor))

        return delays if len(visited) == n else -1