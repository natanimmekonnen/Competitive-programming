# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        def inbound(row,col):
            return (0<=row <len(grid) and 0<=col<len(grid[0]))
        def dfs(grid,visited,row,col):
            visited[row][col]=True
            perimeter=0

            for a,b in directions:
                new_row= row+a
                new_col=col+b
                if not inbound(new_row,new_col) or grid[new_row][new_col]==0:
                    perimeter+=1
                
                if inbound(new_row,new_col) and (not visited[new_row][new_col]) and grid[new_row][new_col]:
                    perimeter+=dfs(grid,visited,new_row,new_col)
            return perimeter
        for ro in range(len(grid)):
            for co in range(len(grid[0])):
                if grid[ro][co]==1:
                    return dfs(grid,visited,ro,co)
                    
        