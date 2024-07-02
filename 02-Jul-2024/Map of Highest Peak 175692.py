# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m=len(isWater)
        n=len(isWater[0])
        answer=[[-1]*n for i in range (m)]
        queue=deque()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(m):
            for j in range(n):
                if isWater[i][j]==1:
                    queue.append((i,j))
                    answer[i][j]=0
        while queue:
            x,y=queue.popleft()
            for dx,dy in directions:
                row,col=x+dx,y+dy
                if 0<=row<m and 0<=col<n and answer[row][col]==-1:
                    queue.append((row,col))
                    answer[row][col]=answer[x][y]+1
            
    
        return answer
        