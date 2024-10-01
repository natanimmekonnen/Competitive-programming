# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/



class handle:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.c = 0

    def crea(self, n):
        if n not in self.parent:
            self.parent[n] = n
            self.rank[n] = 1
            self.c += 1
            return True
        return False

    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, x, y):
        if not self.crea(x):  
            x = self.find(x)
        if not self.crea(y): 
            y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        self.c -= 1

    def nocom(self):
        return self.c

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dj = handle()
        for i, j in stones:
            dj.union(i + 1, -j - 1) 
        return len(stones) - dj.nocom() 
