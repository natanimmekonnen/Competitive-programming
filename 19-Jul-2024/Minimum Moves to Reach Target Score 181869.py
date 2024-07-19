# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        val=0
        while target>1:
            if target %2==0 and maxDoubles>0 :
                target=target//2
                maxDoubles-=1
            else:
                if target%2==1 and maxDoubles>0:
                    target-=1
                else:
                    val+=target-1
                    break
            val+=1
        return val



        