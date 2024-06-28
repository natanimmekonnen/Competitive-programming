# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m = len(maze)
        n = len(maze[0])
        entrance_row, entrance_col = entrance
        visited = set()
        visited.add((entrance_row, entrance_col))
        queue.append((entrance_row, entrance_col))
        path_length = 0
        
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == "." and (nr, nc) not in visited:
                        if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                            if (nr, nc) != (entrance_row, entrance_col): 
                                return path_length + 1
                        
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            
            path_length += 1
        
        return -1