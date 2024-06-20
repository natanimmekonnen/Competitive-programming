# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction=[(0, 1), (0, -1), (1, 0), (-1, 0)]
        n,m=len(grid),len(grid[0])
        comp=0
        visited=set(())
        def dfs(row,col):
            stack=[(row,col)]
            visited.add((row,col))
            while stack:
                row,col=stack.pop()
                for x,y in direction:
                    X=row+x
                    Y=col+y
                    if -1<X<n and -1<Y<m:
                        if (X,Y) not in visited and grid[X][Y]=="1":
                            stack.append((X,Y))
                            visited.add((X,Y))
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=="1" and (row,col)not in visited:
                    dfs(row,col)
                    comp+=1
        return comp




            

        