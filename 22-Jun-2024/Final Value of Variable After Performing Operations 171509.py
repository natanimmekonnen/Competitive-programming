# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        num=0
        for i in range(len(operations)):
            if operations[i]=="--X" or operations[i]=="X--":
                num-=1
            else:
                num+=1
        return num
        