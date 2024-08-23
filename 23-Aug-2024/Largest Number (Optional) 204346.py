# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def solve(i,j):
            if i+j>j+i:
                return -1
               
            if i+j< j+i:
                return 1
                
            else:
                return 0
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(solve))
        
        if nums[0] == '0':
            
            return '0'
        
        
        return ''.join(nums)
