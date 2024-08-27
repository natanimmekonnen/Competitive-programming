# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        array=[0] * (n + 1)
        for i in range(1,n+1):
            count=0
            j=i
            while j!=0:
                count += j & 1
                j >>= 1
            array[i]=count
        return array
                
        