# Problem: Number of Longest Increasing Subsequence - https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        y = [1] * l
        x = [1] * l
        res = 0
        for i in range(l):
            for j in range(i):
                if nums[j] < nums[i]:
                    if x[j] + 1 > x[i]:
                        x[i] = x[j] + 1
                        y[i] = y[j]
                    elif x[j] + 1 == x[i]:
                        y[i] += y[j]
        max_length = max(x)

        for i in range(l):
            if x[i] == max_length:
                res += y[i]
        return res
