# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(number,comb):
            if len(comb)==len(nums):
                ans.append(comb.copy())
                return
            for i in (nums):
                if i in comb:
                    continue
                comb.append(i)
                backtrack(i+1,comb)
                comb.pop()
        backtrack(0,[])
        return ans
        