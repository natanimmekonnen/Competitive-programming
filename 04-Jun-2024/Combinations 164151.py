# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def backtrack(number,comb):
            if len(comb)==k:
                ans.append(comb.copy())
                return
            for i in range(number,n+1):
                comb.append(i)
                backtrack(i+1,comb)
                comb.pop()
        backtrack(1,[])
        return ans
            
        