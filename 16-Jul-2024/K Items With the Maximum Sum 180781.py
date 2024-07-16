# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        val=0
        if k<=numOnes:
            return k
        elif k > numOnes and k<=numOnes +numZeros:
            return numOnes
        elif k>numOnes+numZeros:
            val=k-numOnes-numZeros
            print(val)
            return numOnes-val

        return 0



        