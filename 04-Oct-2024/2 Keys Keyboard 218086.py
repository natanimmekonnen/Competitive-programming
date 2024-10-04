# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        count = 0
        factor = 2
        
        while n > 1:
            while n % factor == 0:
                count += factor
                n //= factor
            factor += 1
            
        return count
        