# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:

        n=len(s)
        if n==0:
            return ""
        dp=[[False]*n for _ in range(n)]
        index=0
        mx=1
        for i in range(n):
            dp[i][i]=True
        for i in range(n-1):
            if s[i]== s[i+1]:
                dp[i][i+1]=True
                index=i
                mx=2
        for i in range(3,n+1):
            for j in range(n-i+1):
                x=j+i-1
                if s[j]==s[x] and dp[j+1][x-1]:
                    dp[j][x]=True
                    index=j
                    mx=i
        return s[index:index+mx]
        
        


