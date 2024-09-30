# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        def find(x):
            if x == parent[x]: return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            X, Y = find(x), find(y)
            if X == Y: return
            parent[Y] = X
        for x, y, _ in roads:
            union(x-1, y-1)
        return min([c for a,b,c in roads if find(0) == find(a-1)])

        