# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents=[i for i in range (len(isConnected))]
        ranks=[1]*(len(isConnected))
        l=len(isConnected)
        def find(x):
            p=x
            while p!=parents[p]:
                parents[p]=parents[parents[p]]
                p=parents[p]
            return p
                
        def union(x1,x2):
            p1,p2=find(x1),find(x2)
            if p1==p2:
                return 0
            if ranks[p1]>ranks[p2]:
                parents[p2]=p1
                ranks[p1]+= ranks[p2]
            else:
                parents[p1]=p2
                ranks[p2]+= ranks[p1]
            return 1
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]==1:
                    l-=union(i,j)
        return l

            

        
        