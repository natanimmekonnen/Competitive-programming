# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        low,high=0,x//2
        while low<=high:
            mid=(low+high)//2
            if mid*mid > x :
                high=mid-1
            elif mid*mid < x :
                low=mid+1
            else:
                return int(mid)
        return int(high)

        