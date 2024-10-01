# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class handle:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
        return self.count


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        l = len(grid)
        ds = handle(l * l * 4) 
        
        for i in range(l):
            for j in range(l):
                bindex = 4 * (i * l + j) 
                if grid[i][j] == '/':
                    ds.union(bindex + 0, bindex + 1)  
                    ds.union(bindex + 2, bindex + 3)  
                elif grid[i][j] == '\\':
                    ds.union(bindex + 0, bindex + 3) 
                    ds.union(bindex + 1, bindex + 2) 
                else:
                    ds.union(bindex + 0, bindex + 1)
                    ds.union(bindex + 1, bindex + 2)
                    ds.union(bindex + 2, bindex + 3)

                if i > 0:
                    ds.union(bindex + 2, bindex - 4 * l + 0) 
                if j > 0:
                    ds.union(bindex + 3, bindex - 4 + 1) 

        return ds.getCount()

