# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        memo={0:0,1:1,3:2}
        def dp(n):
            if n==2:
                return 1
            if n==1 or n==0:
                return n 
            if n not in memo:
                memo[n]=dp(n-1)+dp(n-2)+dp(n-3)
            return memo[n]
        return dp(n)
        