# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr=0
        xorarr=0
        for idx,num in enumerate(nums):
            arr^=num
            xorarr^=idx+1
        return xorarr^arr
            

        