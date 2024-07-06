# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
      
        n = len(board)
    
        def get_position(square):
            row = (square - 1) // n
            col = (square - 1) % n
            if row % 2 == 0:
                return n - 1 - row, col
            else:
                return n - 1 - row, n - 1 - col
    
        visited = set()
        queue = deque([(1, 0)])  
        visited.add(1)
    
        while queue:
            curr, moves = queue.popleft()
        
            if curr == n * n:
                return moves
        
            for next_square in range(curr + 1, min(curr + 6, n * n) + 1):
                r, c = get_position(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
            
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
    
        return -1
