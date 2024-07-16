# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
            if nums[i]+nums[i-1] >nums[i-2] and nums[i]+nums[i-2] >nums[i-1] and nums[i-2]+nums[i-1] >nums[i]:
                return nums[i]+nums[i-1]+nums[i-2]
        return 0
        