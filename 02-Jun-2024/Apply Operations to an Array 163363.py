# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
       
        i = 0
        j = 0
        while i < len(nums): 
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i=i+1
                j=j+1
            else :
                i=i+1
          
        return nums