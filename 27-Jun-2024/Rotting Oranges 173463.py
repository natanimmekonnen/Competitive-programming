# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        time=0
        fresh=0
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    queue.append([i,j])
        while queue and fresh>0:
            for i in range(len(queue)):
                row, col =queue.popleft()
                for r, c in directions:
                    rx , colx= r+row , c+col
                    if(0<=rx<m and 0<=colx<n and grid[rx][colx]==1):
                        grid[rx][colx]=2        
                        queue.append([rx,colx])
                        fresh-=1
            time+=1
        if(fresh!=0):
            return -1
        return time
            

        