# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        i = 0
        result = []
        
        while i < len(nums):
            correct_index = nums[i] - 1
            
            if nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(nums[i])
        
        return result

        