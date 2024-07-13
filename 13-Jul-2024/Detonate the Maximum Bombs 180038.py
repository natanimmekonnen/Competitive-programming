# Problem: Detonate the Maximum Bombs - https://leetcode.com/problems/detonate-the-maximum-bombs/description/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def is_in_range(bomb1, bomb2):
            x1, y1, r1 = bomb1
            x2, y2, _ = bomb2
            return (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2

        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j and is_in_range(bombs[i], bombs[j]):
                    graph[i].append(j)

        def bfs(start):
            visited = [False] * n
            queue = deque([start])
            visited[start] = True
            count = 0
            while queue:
                node = queue.popleft()
                count += 1
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            return count

        max_detonations = 0
        for i in range(n):
            max_detonations = max(max_detonations, bfs(i))

        return max_detonations
                    
        