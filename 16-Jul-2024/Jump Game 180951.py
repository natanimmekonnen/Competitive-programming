# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        val=0
        for i in range(len(nums)):
            if i>val:
                return False
            val=max(val,i+nums[i])
        return True

        
            
            
            
            
        