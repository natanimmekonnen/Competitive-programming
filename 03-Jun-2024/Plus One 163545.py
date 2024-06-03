# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[len(digits)-1]<9:
            digits[len(digits)-1]+=1
            return digits
        else:
            for i in range(len(digits) - 1, -1, -1):
                if digits[i]==9:
                    if i-1<0:
                        val=list((repeat(0, len(digits)+1)))
                        val[0]=1
                        return val
                    digits[i]=0
                else:
                    digits[i]+=1
                    break
            
        return digits
       