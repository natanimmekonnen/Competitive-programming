# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

from collections import deque
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = set()
        queue = deque([(0, 0)])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        map = {
            1: {(1, 0): [], (0, 1): [1, 3, 5], (-1, 0): [], (0, -1): [1, 4, 6]},
            2: {(1, 0): [2, 5, 6], (0, 1): [], (-1, 0): [2, 3, 4], (0, -1): []},
            3: {(1, 0): [2, 5, 6], (0, 1): [], (-1, 0): [], (0, -1): [1, 4, 6]},
            4: {(1, 0): [2, 5, 6], (0, 1): [1, 3, 5], (-1, 0): [], (0, -1): []},
            5: {(1, 0): [], (0, 1): [], (-1, 0): [2, 3, 4], (0, -1): [1, 4, 6]},
            6: {(1, 0): [], (0, 1): [1, 3, 5], (-1, 0): [2, 3, 4], (0, -1): []}
        }

        while queue:
            row, col = queue.popleft()
            if row == m - 1 and col == n - 1:
                return True
            visited.add((row, col))
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                    if (dr, dc) in map[grid[row][col]] and grid[r][c] in map[grid[row][col]][(dr, dc)]:
                        queue.append((r, c))
        return False
