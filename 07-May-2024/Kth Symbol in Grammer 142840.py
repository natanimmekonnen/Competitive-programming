# Problem: Kth Symbol in Grammer - https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def anotherFun(lev,ind,answer):
            if lev==1:
                return answer
            if ind%2==1:
                return anotherFun(lev-1,(ind+1)//2,answer)
            return anotherFun(lev-1,ind//2,1-answer)
        return anotherFun(n,k,0)
        