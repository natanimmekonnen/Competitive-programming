# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
    
        graph = defaultdict(list)
        in_degree = [0] * n
    
        for u, v in richer:
            graph[u].append(v)
            in_degree[v] += 1
        res = [e for e in range(n)]
        quietest = quiet.copy()

        queue = deque()
        for i, degree in enumerate(in_degree):
            if degree == 0:
                queue.append(i)


        while queue:
            cur = queue.popleft()

            for out in graph[cur]:
                if quiet[cur] < quiet[out]:
                    quiet[out] = quiet[cur]
                    res[out] = res[cur]
                in_degree[out] -= 1
                if in_degree[out] == 0:
                    queue.append(out)
        return res 
    
        