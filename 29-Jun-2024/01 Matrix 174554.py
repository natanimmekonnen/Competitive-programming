# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue=deque()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m=len(mat)
        n=len(mat[0])
        dis=[[-1]*n for _ in range(m) ]
        for i in range(m):
            for j in range(n):
                if(mat[i][j]==0):
                    queue.append((i,j))
                    dis[i][j]=0
        while queue:
            r,c=queue.popleft()
            for dr,dc in directions:
                rx,cx=r+dr,c+dc
                if rx<0 or rx==m  or  cx<0 or cx==n or dis[rx][cx]!=-1:
                        continue
                dis[rx][cx]=dis[r][c]+1
                queue.append((rx,cx))
        return dis

        