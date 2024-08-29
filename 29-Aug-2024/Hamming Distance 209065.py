# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        w=x^y
        a=bin(w)[2:]
        count=0
        for i in a:
            if i=='1':
                count+=1

     
        
        return count
            
        