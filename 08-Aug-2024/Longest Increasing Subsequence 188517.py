# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [0] * len(nums)
        def dp(i):
            if i >=len(nums):
                return 0
            if memo[i]==0:
                memo[i]=1
                for j in range(i+1,len(nums)):
                    if nums[j]>nums[i]:
                        memo[i]=max(1+dp(j),memo[i])
            return memo[i]
        ml=0
        for i in range(len(nums)):
            ml=max(dp(i),ml)
        return ml

        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    memo[i] = max(memo[i], memo[j] + 1)
        
        return max(memo)

        