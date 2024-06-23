# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx=0
        formermax=0
        for i in range(len(nums)):
            if(nums[i]==1):
                maxx+=1
            elif(nums[i]==0):
                formermax= max(formermax,maxx)
                maxx=0
               
        return max(formermax,maxx)

        