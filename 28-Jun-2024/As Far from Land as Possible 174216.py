# Problem: As Far from Land as Possible - https://leetcode.com/problems/as-far-from-land-as-possible/description/

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue=deque()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m=len(grid)
        n=len(grid[0])
        far=-1
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    queue.append((i,j))
        if len(queue) == m * n or not queue :
            return -1
        while queue:
            far+=1
            for _ in range(len(queue)):
                r,c=queue.popleft()
                for dr,dc in directions:
                    rx,cx=r+dr,c+dc
                    if rx<0 or rx==m  or  cx<0 or cx==n or grid[rx][cx]!=0:
                        continue
                    grid[rx][cx]=1
                    queue.append((rx,cx))

        return far


        
        