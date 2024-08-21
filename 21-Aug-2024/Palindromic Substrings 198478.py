# Problem: Palindromic Substrings - https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo = [[None] * n for _ in range(n)]

        def isPalindrome(i, j):
            if i > j:
                return False
            if i == j:
                return True
            if memo[i][j] is not None:
                return memo[i][j]
            
            if s[i] == s[j]:
                if j - i == 1 or isPalindrome(i + 1, j - 1):
                    memo[i][j] = True
                    return True
            
            memo[i][j] = False
            return False

        count = 0
        for i in range(n):
            for j in range(i, n):
                print(s[i],s[j])
                if isPalindrome(i, j):

                    count += 1

        return count

            