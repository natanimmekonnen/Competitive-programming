# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        var=bin(num)[2:]
        new=""
        for i in var:
            if i=='1':
                new+='0'
                
            else:
                new+='1'
        print(int(new,2))
        return (int(new,2))
        