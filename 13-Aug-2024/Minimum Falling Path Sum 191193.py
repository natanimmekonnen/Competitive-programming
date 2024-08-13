# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        dp = matrix[0][:]
        

        for i in range(1, n):
            new_dp = [0] * n
            
            for j in range(n):
                left = dp[j - 1] if j > 0 else float('inf')
                middle = dp[j]
                right = dp[j + 1] if j < n - 1 else float('inf')
                
                new_dp[j] = matrix[i][j] + min(left, middle, right)
            
            dp = new_dp
        return min(dp)