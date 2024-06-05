# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    
    def splitString(self, s: str) -> bool:
        array= []
        def backtrack(num):
            if num>=len(s):
                for i in range (1,len(array)):
                    if array[i-1]-array[i]!=1:
                        return False
                return len(array)>=2
            for i in range (num+1,len(s)+1):
                hold= int(s[num:i])
                if not array or hold - array[-1] == -1:
                    array.append(hold)
                    if backtrack(i):
                        return True
                    array.pop()
            return False
        return backtrack(0)

            
        