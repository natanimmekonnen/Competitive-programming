# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(number,subs):
            ans.append(subs.copy())
            for i in range(number,len(nums)):
                subs.append(nums[i])
                backtrack(i+1,subs)
                subs.pop()
        backtrack(0,[])
        return ans
            
        