# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
         
        memo = {}

        def dp(i, current_sum):
            if i>=len(nums):
                return 1 if current_sum==target else 0
            if (i,current_sum) not in memo:
                add=dp(i+1,current_sum+nums[i])
                sub=dp(i+1,current_sum-nums[i])
                memo[(i,current_sum)]=add+sub
            return memo[(i,current_sum)]
        
        return dp(0, 0)

            