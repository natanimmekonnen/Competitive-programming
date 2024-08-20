# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(houses):
            n = len(houses)
            if n == 0:
                return 0
            if n == 1:
                return houses[0]
        
            dp = [0] * n
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])
            
            return dp[-1]
        
        n = len(nums)
        if n == 1:
            return nums[0]
    
        return max(dp(nums[:-1]), dp(nums[1:]))
        